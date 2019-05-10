from django.contrib import admin
from .models import (AboutMe, ContactInformation, Introduction, Projects,
                     Resume, Subscription)

admin.site.register(AboutMe)
admin.site.register(ContactInformation)
admin.site.register(Introduction)
admin.site.register(Projects)
admin.site.register(Resume)
admin.site.register(Subscription)
