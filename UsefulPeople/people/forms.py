from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from people.models import Message, UserAccount, Skills, Experience, Education, Achievements

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

class ResumeForm(ModelForm):

    class Meta:
        model = UserAccount
        fields = ['first_name_u', 'last_name_u', 'profession', 
            'country', 'city', 'university', 'photo', 
            'additional_information',
        ]

    # def __init__(self, *args, **kwargs):
    #     super(ResumeForm, self).__init__(*args, **kwargs)
    #     self.fields['photo'].widget = forms.FileInput(attrs={
    #         'class': 'input_photo',
    #         })
    #     self.fields['first_name_u'].widget = forms.TextInput(attrs={
    #         'class': 'input_log',
    #         })
    #     self.fields['last_name_u'].widget = forms.TextInput(attrs={
    #         'class': 'input_passwd',
    #         })
    #     self.fields['profession'].widget = forms.TextInput(attrs={
    #         'class': 'input_passwd',
    #         })
    #     self.fields['country'].widget = forms.TextInput(attrs={
    #         'class': 'input_passwd',
    #         })
    #     self.fields['city'].widget = forms.TextInput(attrs={
    #         'class': 'input_passwd',
    #         })
    #     self.fields['university'].widget = forms.TextInput(attrs={
    #         'class': 'input_passwd',
    #         })
    #     self.fields['skills'].widget = forms.TextInput(attrs={
    #         'class': 'input_skill',
    #         })
    #     self.fields['experience'].widget = forms.TextInput(attrs={
    #         'class': 'input_passwd',
    #         })
    #     self.fields['additional_education'].widget = forms.TextInput(attrs={
    #         'class': 'input_passwd',
    #         })
    #     self.fields['achievements'].widget = forms.TextInput(attrs={
    #         'class': 'input_passwd',
    #         })
    #     self.fields['additional_information'].widget = forms.Textarea(attrs={
    #         'class': 'input_addinfo',
    #         })

    # def save(self, commit=True):
    #     old_save_m2m = self.save_m2m
    #     def save_m2m():
    #         old_save_m2m()

class SkillsForm(ModelForm):

    class Meta:
        model = Skills
        fields = '__all__'

class ExperienceForm(ModelForm):

    class Meta:
        model = Experience
        fields = '__all__'

class EducationForm(ModelForm):

    class Meta:
        model = Education
        fields = '__all__'

class AchievementsForm(ModelForm):

    class Meta:
        model = Achievements
        fields = '__all__'