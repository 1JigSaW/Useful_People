from django.shortcuts import render, redirect
from .forms import UsersForm, UsersRegistrationForm
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

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
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'registration_done.html', {'form': form})
                else:
                    return HttpResponse('Disabled account')

            else:
                return HttpResponse('Invalid login')
        else:
            return render(request, 'authorisation.html', {'form': form})
    else:
        form = UsersForm()
        return render(request, 'authorisation.html', {'form': form})