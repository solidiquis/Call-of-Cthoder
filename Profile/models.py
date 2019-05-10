from django.db import models

class Introduction(models.Model):
    intro = models.TextField(max_length=275, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-upload_date']
        get_latest_by = 'upload_date'

class AboutMe(models.Model):
    description = models.TextField(max_length=756, blank=True)
    profile_picture = models.ImageField(
        upload_to='Profile/AboutMe/',
        blank=True,
        null=True,
        )
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post_date}'

    class Meta:
        ordering = ['-post_date']
        get_latest_by = 'post_date'

class Projects(models.Model):
    title = models.CharField(max_length=45, blank=True)
    summary = models.TextField(max_length=219, blank=True)
    project_picture = models.ImageField(
        upload_to='Profile/Projects/',
        blank=True,
        null=True,
        )
    project_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Resume(models.Model):
    resume_pdf = models.FileField(
        upload_to='Profile/Resume/',
        blank=True,
        null=True,
        )

    def __str__(self):
        return 'Resume'

    class Meta():
        ordering = ['-pk']

class ContactInformation(models.Model):
    email = models.EmailField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return 'Contact Info'

class Subscription(models.Model):
    user_email = models.EmailField(blank=False, null=True, unique=True)

    def __str__(self):
        return self.user_email
