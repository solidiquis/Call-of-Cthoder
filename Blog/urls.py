from django.urls import path
from .views import (BlogIndexView, Login, LogOut, ReplyHandler, Registration,
                    UpdateDeleteComment, VotesHandler)

app_name = 'Blog'

urlpatterns = [
    path('',
        BlogIndexView.as_view(),
        name='Blog_index',
        ),
    path(
        'Comment/Delete/<int:comment_pk>/',
        UpdateDeleteComment,
        name='Delete_comment',
        ),
    path(
        'Comment/Update/<int:comment_pk>/',
        UpdateDeleteComment,
        name='Update_comment',
        ),
    path(
        'Login/',
        Login.as_view(),
        name='Login',
        ),
    path(
        'Login/<str:error>/',
        BlogIndexView.as_view(),
        name="Login_error",
        ),
    path(
        'Logout/',
        LogOut.as_view(),
        name='Logout',
        ),
    path(
        'Reply/<str:parent_comment_pk>/',
        ReplyHandler,
        name='Reply',
        ),
    path(
        'Registration/',
        Registration,
        name='Registration',
        ),
    path(
        'Registration/<str:error_type>/',
         BlogIndexView.as_view(),
         name='Registration_error',
        ),
    path(
        'Vote/<int:comment_pk>/<str:vote_type>/',
        VotesHandler,
        name='Vote',
        ),
]
