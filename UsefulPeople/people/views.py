from django.shortcuts import render, redirect
from .forms import UsersForm, UsersRegistrationForm

def index(request):
    return render(request, 'index.html')

def registration(request):
    errors = []
    if request.method == 'POST':
        user_form = UsersRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save()
            return render(request, 'registration_done.html', {'new_user': new_user})
        else:
            form = UsersRegistrationForm()
            errors.append('Пароли не совпадают!')
            return render(request, 'registration.html', 
                {'form': form,
                'errors': errors,
                })
    else:
        form = UsersRegistrationForm()
        return render(request, 'registration.html', {'form': form})

def authorisation(request):
    form = UsersForm()
    return render(request, 'authorisation.html', {'form': form})