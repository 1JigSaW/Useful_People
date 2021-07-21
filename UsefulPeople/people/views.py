from django.shortcuts import render, redirect
from .forms import UsersForm, UsersRegistrationForm
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'index.html')

def registration(request):
    errors = []
    if request.method == 'POST':
        user_form = UsersRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save()
            new_user.active = True
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
    errors = []
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = request.POST.get('login')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'registration_done.html', {'form': form,
                        'errors': errors})
                else:
                    errors.append('Несуществующий аккаунт')
                    return HttpResponse('Disabled account')

            else:
                errors.append('Неправильый логин')
                return HttpResponse('Invalid login')
        else:
            errors.append('Введите корректные данные')
            form = UsersForm()
            return render(request, 'authorisation.html', {'form': form,
                'errors': errors})
    else:
        form = UsersForm()
    return render(request, 'authorisation.html', {'form': form,
        'errors': errors})