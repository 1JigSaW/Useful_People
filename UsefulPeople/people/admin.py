from django.contrib import admin
from people.models import Skills, Experience, Education, Achievements, UserAccount

class UserAccountAdmin(admin.ModelAdmin):
	readonly_fields = ('id',)

admin.site.register(Skills)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Achievements)
admin.site.register(UserAccount, UserAccountAdmin)