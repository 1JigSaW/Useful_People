from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Users

class UsersForm(forms.ModelForm):
    login = forms.CharField(
        widget = forms.TextInput(attrs={'class': "input_log"}),
        )
    class Meta:
        model = Users
        fields = ('login', 'password',)
        labels = {
            'login': _('Логин'),
            'password': _('Пароль')
        }