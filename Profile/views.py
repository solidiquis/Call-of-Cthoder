from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from CallofCthoder.settings import STATIC_DIR
from Blog.models import BlogPost
from .models import (AboutMe, ContactInformation, Introduction, Subscription,
                    Projects, Resume)

class IndexView(TemplateView):
    template_name = 'Profile/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Generates context for the blurb
        if Introduction.objects.first() is not None:
            blurb = Introduction.objects.latest()
        else:
            blurb = 'Placeholder'

        context['blurb'] = blurb

        # Generates context for the about me section
        if AboutMe.objects.first() is not None:
            about_me = AboutMe.objects.first()
        else:
            about_me = AboutMe.objects.none()

        context['about_me'] = about_me

        # Generates context for the project section
        context['projects'] = Projects.objects.all()

        # Generate the context for the most recent blogpost preview
        context['recent_blogpost'] = BlogPost.objects.first()

        return context

def ResumeView(request):
    """
    View for displaying Resume.
    """
    try:
        resume = Resume.objects.all().first()
        response = HttpResponse(resume.resume_pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="foo.pdf"'
    except:
        response = HttpResponse('Error')
    return response

def SubscriptionHandler(request):

    if request.method == 'POST' and request.is_ajax():
        user_email = request.POST['user_email']
        Subscription.objects.create(user_email=user_email)

    return JsonResponse({'success_message': 'Thanks for subscribing!'})
