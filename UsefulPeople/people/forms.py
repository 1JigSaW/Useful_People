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