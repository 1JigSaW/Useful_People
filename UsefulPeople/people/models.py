from django.db import models

class Users(models.Model):
	login = models.CharField(max_length=50, blank=False)
	email = models.CharField(max_length=50, blank=False)
	password = models.CharField(max_length=20, blank=False)
	password2 = models.CharField(max_length=20, blank=False, editable=False)

	def __str__(self):
		return f"{self.login}"

	class Meta:
		verbose_name = 'Читатель'
		verbose_name_plural = 'Читатели'

