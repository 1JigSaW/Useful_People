from django.shortcuts import render, redirect
from .forms import UsersForm, UsersRegistrationForm
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import UserAccount, Skills, Experience, Education, Achievements
from django.urls import reverse

def index(request):
    if request.user.is_authenticated:
        return redirect('main')
    return render(request, 'index.html')

def main(request):
    accounts = UserAccount.objects.all()
    return render(request, 'main.html', {'accounts': accounts,})

def registration(request):
    if request.user.is_authenticated:
        return redirect('main')
    if request.method == 'POST':
        user_form = UsersRegistrationForm(request.POST)
        if user_form.is_valid():
            form = user_form.save()
            return render(request, 'registration_done.html', {'form': form})
        else:
            form = UsersRegistrationForm()
            return render(request, 'registration.html', 
                {'form': form,
                'user_form': user_form})
    else:
        form = UsersRegistrationForm()
        return render(request, 'registration.html', {'form': form})

def authorisation(request):
    if request.user.is_authenticated:
        return redirect('main')
    errors = []
    if request.method == 'POST':
        form = UsersForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                print(form)
                return redirect('main')
            else:
                errors.append('Данные не верны')
                return render(request, 'authorisation.html', {'form': form,
                    'errors': errors})

        else:
            errors.append('Такого пользователя не существует')
            return render(request, 'authorisation.html', {'form': form,
                'errors': errors})
    else:
        form = UsersForm()
        return render(request, 'authorisation.html', {'form': form,
            'errors': errors})

def page(request):
    accounts = UserAccount.objects.all()
    return render(request, 'page.html', {'accounts': accounts,})