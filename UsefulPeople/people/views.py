from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def registartion(request):
    return render(request, 'registartion.html')

def authorisation(request):
    return render(request, 'authorisation.html')