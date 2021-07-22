from django.db import models

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
	skills = models.CharField(max_length=50)

class Experience(models.Model):
	company_name = models.CharField(max_length=50)
	position = models.CharField(max_length=100)
	years_of_work = models.IntegerField()
	mounth_of_work = models.IntegerField()
	photo_work = models.ImageField(upload_to='photo_works')

class Education(models.Model):
	university_name = models.CharField(max_length=100)
	direction = models.CharField(max_length=50)
	start_training = models.DateField()
	end_training = models.DateField()

class Achievements(models.Model):
	topic = models.CharField(max_length=100)
	description = models.TextField()

class UserAccount(models.Model):
	# user_id = models.ForeignKey(User, on_delete=models.CASCADE,)
	first_name = models.CharField(max_length=50, blank=False)
	last_name = models.CharField(max_length=50, blank=False)
	profession = models.CharField(max_length=100)
	country = models.CharField(max_length=40)
	city = models.CharField(max_length=40)
	university = models.CharField(max_length=100)
	photo = models.ImageField(upload_to='photos')
	skills = models.ManyToManyField(Skills)
	experience = models.ManyToManyField(Experience)
	additional_education = models.ManyToManyField(Education)
	achievements = models.ManyToManyField(Achievements)
	additional_information = models.TextField()

