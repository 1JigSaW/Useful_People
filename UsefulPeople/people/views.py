from django.shortcuts import render
from .forms import UsersForm

def index(request):
    return render(request, 'index.html')

def registration(request):
    return render(request, 'registration.html')

def authorisation(request):
    form = UsersForm()
    return render(request, 'authorisation.html', {'form': form})