from django.shortcuts import render, redirect, get_object_or_404
from .forms import UsersForm, UsersRegistrationForm, MessageForm
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import UserAccount, Skills, Experience, Education, Achievements, Chat
from django.db.models import Q
from django.urls import reverse
from django.views.generic import View

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

def page(request, id):
    account = UserAccount.objects.get(pk=id)
    return render(request, 'page.html', {'account': account,})

def search(request):
    comment = ''
    if 'q' in request.GET and request.GET['q']:
        query = request.GET['q']
        try:
            accounts = UserAccount.objects.filter(
                Q(skills__icontains=query) | Q(experience__icontains=query) | Q(additional_education__icontains=query) | Q(achievements__icontains=query) | Q(additional_information__icontains=query)
            )
            print(accounts)
            context = { 'accounts': accounts }
            print(accounts)
        except :
            accounts = UserAccount.objects.all()
            comment = 'Ничего не найдено'
            context = { 'accounts': accounts, 'comment': comment }
        return render(request, 'main.html', context)
    else:
        accounts = UserAccount.objects.all()
        comment = 'Повторите запрос'
        context = { 'accounts': accounts, 'comment': comment }
        return render(request, 'main.html', context)

def chats(request):
    chats = Chat.objects.filter(members__in=[request.user.id])
    return render(request, 'chats.html', {'user_profile': request.user, 
        'chats': chats})

class MessagesView(View):
    def get(self, request, chat_id):
        try:
            chat = Chat.objects.get(id=chat_id)
            if request.user in chat.members.all():
                chat.message_set.filter(is_readed=False).exclude(author=request.user).update(is_readed=True)
            else:
                chat = None
        except Chat.DoesNotExist:
            chat = None
 
        return render(
            request,
            'messages.html',
            {
                'user_profile': request.user,
                'chat': chat,
                'form': MessageForm()
            }
        )
 
    def post(self, request, chat_id):
        form = MessageForm(data=request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat_id = chat_id
            message.author = request.user
            message.save()
        return redirect(reverse('messages', kwargs={'chat_id': chat_id}))

class CreateDialogView(View):
    def get(self, request, user_id):
        chats = Chat.objects.filter(members__in=[request.user.id, user_id], type_c=Chat.DIALOG).annotate(c=count('members')).filter(c=2)
        if chats.count() == 0:
            chat = Chat.objects.create()
            chat.members.add(request.user)
            chat.members.add(user_id)
        else:
            chat = chats.first()
        return redirect(reverse('users:messages', kwargs={'chat_id': chat.id}))