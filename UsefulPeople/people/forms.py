from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Users

class UsersForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = ('login', 'password',)
        labels = {
            'login': _('Логин'),
            'password': _('Пароль')
        }

    def __init__(self, *args, **kwargs):
        super(UsersForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={
            'class': 'input_log',
            })
        self.fields['password'].widget = forms.TextInput(attrs={
            'class': 'input_passwd',
            })

class UsersRegistrationForm(forms.ModelForm):
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={
            'class': 'input_passwd2_2',
            }))

    class Meta:
        model = Users
        fields = ('login', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super(UsersRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={
            'class': 'input_log_2',
            })
        self.fields['password'].widget = forms.TextInput(attrs={
            'class': 'input_passwd_2',
            })
        self.fields['email'].widget = forms.TextInput(attrs={
            'class': 'input_email_2',
            })

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']