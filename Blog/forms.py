from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Comment
from .mixins import FormFields


class LoginForm(forms.Form, FormFields):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.get_fields():
            self.fields[field].label = ''
            self.fields[field].widget.attrs.update({
                'class': 'login-styles',
                'placeholder': field,
                })

class RegistrationForm(UserCreationForm):
    user_fields = ('username', 'password1', 'password2')

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.user_fields:
            if field == 'password1':
                placeholder = 'password'
            elif field == 'password2':
                placeholder = 'password confirmation'
            else:
                placeholder = 'username'
            self.fields[field].label = ''
            self.fields[field].widget.attrs.update({
                'class': 'registration-styles',
                'placeholder': placeholder,
                })

class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['body'].label = ''

    class Meta:
        model = Comment
        fields = ('body', )

class EditCommentForm(forms.Form):
    content = forms.CharField(widget=CKEditorWidget(config_name='edit_comment'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].label = ''
