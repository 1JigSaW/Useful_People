from django.shortcuts import render, redirect
from .forms import UsersForm, UsersRegistrationForm
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(request, 'index.html')

def registration(request):
    if request.method == 'POST':
        user_form = UsersRegistrationForm(request.POST)
        if user_form.is_valid():
            form = user_form.save()
            return render(request, 'registration_done.html', {'form': form, 
                'user_form': user_form})
        else:
            form = UsersRegistrationForm()
            return render(request, 'registration.html', 
                {'form': form,
                'user_form': user_form})
    else:
        form = UsersRegistrationForm()
        return render(request, 'registration.html', {'form': form})

def authorisation(request):
    errors = []
    if request.method == 'POST':
        form = UsersForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'main.html', {'form': form})
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

def main(request):
    return render(request, 'main.html')
