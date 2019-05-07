from django.contrib.auth import get_user_model
from django.contrib.auth.views import LogoutView, LoginView
from django.core import serializers
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from .forms import CommentForm, LoginForm, RegistrationForm
from .models import BlogPost, Comment
import re

def Registration(request):

    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        username = request.POST['username']
        pw_1 = request.POST['password1']
        pw_2 = request.POST['password2']

        if pw_1 != pw_2:
            return HttpResponseRedirect(
            reverse_lazy('Blog:Registration_error', args=['pw_mismatch'])
            )
        try:
            get_object_or_404(get_user_model(), username=username)
            return HttpResponseRedirect(
            reverse_lazy('Blog:Registration_error', args=['user_exists'])
            )
        except:
            pass

        if registration_form.is_valid():
            new_user = registration_form.save()
        else:
            return HttpResponseRedirect(
            reverse_lazy('Blog:Registration_error', args=['user_exists'])
            )

    return HttpResponseRedirect(reverse_lazy('Blog:Blog_index'))

class Login(LoginView):
    template_name = 'Blog/blog_index.html'

    def get_success_url(self):
        return reverse_lazy('Blog:Blog_index')

    def form_invalid(self, form):
        return HttpResponseRedirect(
            reverse_lazy('Blog:Login_error', args=['login_error'])
        )

class LogOut(LogoutView):
    next_page = reverse_lazy('Blog:Blog_index')

class BlogIndexView(FormView, ListView):
    template_name = 'Blog/blog_index.html'
    context_object_name = 'blogposts'
    paginate_by = 1
    form_class = CommentForm
    redirect_field_name = reverse_lazy('Blog:Blog_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_form'] = LoginForm
        context['registration_form'] = RegistrationForm

        try:
            error_type = self.kwargs['error_type']
            if error_type == 'pw_mismatch':
                context['pw_mismatch'] = True
            elif error_type == 'user_exists':
                context['user_exists'] = True
            elif error_type == 'invalid_fields':
                context['invalid_fields'] = True
        except KeyError:
            pass

        try:
            if self.kwargs['error']:
                context['login_error'] = True
        except KeyError:
            pass

        return context

    def get_queryset(self):
        return BlogPost.objects.all()

    def get_page_number(self, return_type):
        regex = r'\?page=\d*'
        pattern = re.compile(regex)
        referer = self.request.META['HTTP_REFERER']
        try:
            query_str = pattern.search(referer).group(0)
        except AttributeError:
            query_str = '?page=1'

        page_num = query_str[-1]

        if return_type == 'query_string':
            return query_str
        elif return_type == 'page_num':
            return page_num

    def get_success_url(self):
        query_str = self.get_page_number('query_string')
        return reverse_lazy('Blog:Blog_index') + query_str

    def get_blog_post(self):
        paginator = Paginator(self.get_queryset(), 1)
        obj_list = paginator.page(self.get_page_number('page_num'))
        blog_post = obj_list[0]
        return blog_post

    def form_valid(self, form):
        comment_form = CommentForm(self.request.POST)
        comment = comment_form.save(commit=False)
        comment.blogpost = self.get_blog_post()
        comment.user = self.request.user
        comment.save()

        if self.request.is_ajax():
            template_context = {
                'commented': True,
                'comments': self.get_blog_post().comments.all(),
                'user': self.request.user,
                }
            comments = render_to_string(
                'Blog/comments.html',
                context=template_context,
                request=self.request,
                )
            json_context = {'comments': comments}
            return JsonResponse(json_context)

        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url())

def ReplyView(request, parent_comment_pk):
    response = HttpResponseRedirect(reverse_lazy('Blog:Blog_index'))

    parent_comment = Comment.objects.get(pk=parent_comment_pk)
    parent_post = parent_comment.blogpost

    if request.method == 'POST':
        Comment.objects.create(
            user=request.user,
            blogpost=parent_post,
            is_reply=True,
            parent_comment=parent_comment,
            reply_body=request.POST['reply_body']
        )

    if request.is_ajax():
        template_context = {
            'replied': True,
            'parent_comment': parent_comment,
        }
        template = render_to_string(
            'Blog/replies.html',
            template_context,
            request=request,
            )
        response = JsonResponse({'replies': template})

    return response

def VotesView(request, comment_pk, vote_type):
    response = HttpResponseRedirect(reverse_lazy('Blog:Blog_index'))

    user = request.user
    comment = get_object_or_404(Comment, pk=comment_pk)

    if user.is_authenticated:
        comment.increment_vote(user, vote_type)

    if request.is_ajax():
        json_context = {'score': comment.score, 'id': comment.pk}
        response = JsonResponse(json_context)

    return response

def DeleteComment(request, comment_pk):
    response = HttpResponseRedirect(reverse_lazy('Blog:Blog_index'))

    comment = get_object_or_404(Comment, pk=comment_pk)
    blogpost = comment.blogpost
    comment.delete()

    if request.is_ajax():
        template_context = {
            'commented': True,
            'comments': blogpost.comments.all(),
            'user': request.user,
            }
        comment_sec = render_to_string('Blog/comments.html', template_context)
        response = JsonResponse({'comments': comment_sec})

    return response

def UpdateComment(request, comment_pk):
    pass
