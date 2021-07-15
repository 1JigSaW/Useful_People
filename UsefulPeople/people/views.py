from django.shortcuts import render
from .forms import UsersForm, UsersRegistrationForm

def index(request):
    return render(request, 'index.html')

def registration(request):
    form = UsersRegistrationForm()
    return render(request, 'registration.html', {'form': form})

def authorisation(request):
    form = UsersForm()
    return render(request, 'authorisation.html', {'form': form})