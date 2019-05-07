from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.text import slugify

class Blurb(models.Model):
    blurb = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

class BlogPost(models.Model):
    superuser = models.ForeignKey(
        get_user_model(),
        related_name='blogposts',
        on_delete=models.CASCADE,
        )
    title = models.CharField(max_length=45, blank=False)
    photo = models.ImageField(upload_to="Blog/BlogPost/", blank=True, null=True)
    photo_subtitle = models.TextField(blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    body = RichTextField(blank=False, config_name='ckeditor')
    preview = models.CharField(max_length=170, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def get_absolute_url(self):
        print(reverse('Blog:blog_index', args=[self.slug]))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta():
        ordering = ["-posted_at"]

class Comment(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        related_name='comments',
        on_delete=models.CASCADE,
        )
    blogpost = models.ForeignKey(
        BlogPost,
        related_name='comments',
        on_delete=models.CASCADE,
        )
    body = RichTextField(blank=False, config_name='ckeditor_comments')
    commented_at = models.DateTimeField(auto_now_add=True)
    votes = models.ManyToManyField(get_user_model(), blank=True)
    score = models.IntegerField(default=0)
    is_reply = models.BooleanField(default=False, null=True)
    parent_comment = models.ForeignKey(
        'self',
        related_name='replies',
        null=True,
        on_delete=models.CASCADE,
    )
    reply_body = models.TextField(blank=False, null=True)

    def __str__(self):
        return f'{self.blogpost.title}: {self.commented_at}'

    def increment_vote(self, user, vote_type):

        if user not in self.votes.all(): # User's first time voting
            self.votes.add(user)

            if vote_type == 'upvote':
                self.score += 1
                VoteType.objects.create(
                    user=user,
                    comment=self,
                    vote_type='upvote',
                    )
            elif vote_type == 'downvote':
                self.score -= 1
                VoteType.objects.create(
                    user=user,
                    comment=self,
                    vote_type='downvote',
                    )

        else: # If user had already voted previously
            previous_vote_obj = get_object_or_404(
                VoteType,
                user=user,
                comment=self,
            )
            previous_vote = previous_vote_obj.vote_type
            if vote_type == 'upvote':
                if previous_vote == 'upvote':
                    self.score -= 1
                    vote_type = ''
                elif previous_vote == 'downvote':
                    self.score += 2
                else:
                    self.score += 1
            elif vote_type == 'downvote':
                if previous_vote == 'downvote':
                    self.score += 1
                    vote_type = ''
                elif previous_vote == 'upvote':
                    self.score -= 2
                else:
                    self.score -= 1

            previous_vote_obj.vote_type = vote_type
            previous_vote_obj.save()

        self.save()

    def show_score(self):
        return self.score

    def show_vote_count(self):
        return self.votes.count()

    class Meta:
        ordering = ['-commented_at']
        get_latest_by = 'commented_at'

class VoteType(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        related_name='vote_types',
        on_delete=models.CASCADE,
        )
    comment = models.ForeignKey(
        Comment,
        related_name='vote_types',
        on_delete=models.CASCADE,
        )
    vote_type = models.CharField(max_length=20, blank=True, null=True)
