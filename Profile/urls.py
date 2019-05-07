from django.urls import path

from .views import IndexView, SubscriptionHandler, ResumeView

app_name = 'Profile'

urlpatterns = [
    path(
        '',
        IndexView.as_view(),
        name='index',
        ),
    path(
        'BNResume/',
        ResumeView,
        name='resume',
        ),
    path(
        'Subscription/',
        SubscriptionHandler,
        name='subscription',
        ),
]
