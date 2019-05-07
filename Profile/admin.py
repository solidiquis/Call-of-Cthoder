from django.contrib import admin
from .models import AboutMe, Subscription, Projects, Resume, ContactInformation

admin.site.register(AboutMe)
admin.site.register(Subscription)
admin.site.register(Projects)
admin.site.register(Resume)
admin.site.register(ContactInformation)
