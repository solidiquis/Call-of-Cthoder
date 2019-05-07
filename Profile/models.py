from django.db import models

class AboutMe(models.Model):
    description = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to='Profile/AboutMe/',
        blank=True,
        null=True,
        )

    def __str__(self):
        return 'About me'

class Projects(models.Model):
    title = models.CharField(max_length=45, blank=True)
    summary = models.TextField(blank=True)
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
