"""UsefulPeople URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from people import views
from people.views import index, authorisation, registration, main, page, search
from people.views import chats, user_logout, account, create_resume
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index, name='index'),
    path('registration/', registration, name='registration'),
    path('authorisation/', authorisation, name='authorisation'),
    path('logout/', user_logout, name='user_logout'),
    path('', main, name='main'),
    path('account/', account, name='account'),
    path('<id>/', page, name='page'),
    path('search', search, name='search'),
    path('account/create_resume', create_resume, name='create_resume'),
    path('chats', chats, name='chats'),
    path('chats/create/<user_id>', views.CreateDialogView.as_view(), name='chat_create'),
    path('chats/<chat_id>', views.MessagesView.as_view(), name='messages'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
