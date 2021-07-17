from django.contrib import admin
from people.models import Users

class UsersAdmin(admin.ModelAdmin):
	list_display = ('login', 'email', 'password')

admin.site.register(Users)
