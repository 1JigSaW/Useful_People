from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from people.models import Message

class UsersForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ('username', 'password',)
        labels = {
            'username': _('Логин'),
            'password': _('Пароль')
        }

    def __init__(self, *args, **kwargs):
        super(UsersForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'input_log',
            })
        self.fields['password'].widget = forms.TextInput(attrs={
            'class': 'input_passwd',
            })

class UsersRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UsersRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'input_log_2',
            })
        self.fields['password1'].widget = forms.TextInput(attrs={
            'class': 'input_passwd_2',
            })
        self.fields['email'].widget = forms.TextInput(attrs={
            'class': 'input_email_2',
            })
        self.fields['password2'].widget = forms.TextInput(attrs={
            'class': 'input_passwd2_2',
            })

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['message']
        labels = {'message': ""}