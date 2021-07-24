from django.db import models
from django.contrib.auth.models import User
# class Users(models.Model):
# 	login = models.CharField(max_length=50, blank=False)
# 	email = models.CharField(max_length=50, blank=False)
# 	password = models.CharField(max_length=20, blank=False)
# 	password2 = models.CharField(max_length=20, blank=False, editable=False)

# 	def __str__(self):
# 		return f"{self.login}"

# 	class Meta:
# 		verbose_name = 'Читатель'
# 		verbose_name_plural = 'Читатели'
class Skills(models.Model):
	title = models.CharField(max_length=50)

	def __str__(self):
		return f"{self.skills}"

	class Meta:
		verbose_name = 'Навык'
		verbose_name_plural = 'Навыки'

class Experience(models.Model):
	company_name = models.CharField(max_length=50)
	position = models.CharField(max_length=100)
	years_of_work = models.IntegerField()
	mounth_of_work = models.IntegerField()
	photo_work = models.ImageField(upload_to='static/photo_works')

	def __str__(self):
		return f"{self.company_name}"

	class Meta:
		verbose_name = 'Опыт работы'
		verbose_name_plural = 'Опыт работ'


class Education(models.Model):
	university_name = models.CharField(max_length=100)
	direction = models.CharField(max_length=50)
	start_training = models.DateField()
	end_training = models.DateField()

	def __str__(self):
		return f"{self.university_name}"

	class Meta:
		verbose_name = 'Дополнительное образование'
		verbose_name_plural = 'Дополнительные образования'

class Achievements(models.Model):
	topic = models.CharField(max_length=100)
	description = models.TextField()

	def __str__(self):
		return f"{self.topic}"

	class Meta:
		verbose_name = 'Достижение'
		verbose_name_plural = 'Достижения'

class UserAccount(models.Model):
	# user_id = models.ForeignKey(User, on_delete=models.CASCADE,)
	first_name = models.CharField(max_length=50, blank=False)
	last_name = models.CharField(max_length=50, blank=False)
	profession = models.CharField(max_length=100)
	country = models.CharField(max_length=40)
	city = models.CharField(max_length=40)
	university = models.CharField(max_length=100)
	photo = models.ImageField(upload_to='static/photos')
	skills = models.ManyToManyField(Skills)
	experience = models.ManyToManyField(Experience)
	additional_education = models.ManyToManyField(Education)
	achievements = models.ManyToManyField(Achievements)
	additional_information = models.TextField()

	def __str__(self):
		return f'{self.first_name}, {self.last_name}'

	class Meta:
		verbose_name = 'Аккаунт'
		verbose_name_plural = 'Аккаунты'

