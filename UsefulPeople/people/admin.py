from django.contrib import admin
from people.models import Skills, Experience, Education, Achievements, UserAccount

# class UsersAdmin(admin.ModelAdmin):
# 	list_display = ('login', 'email', 'password')

# admin.site.register(Users)

admin.site.register(Skills)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Achievements)
admin.site.register(UserAccount)