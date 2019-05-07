from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import BlogPost, Blurb, Comment, VoteType

admin.site.register(Blurb)
admin.site.register(Comment)
admin.site.register(VoteType)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        kwargs['queryset'] = get_user_model().objects.filter(username='solidiquis')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
