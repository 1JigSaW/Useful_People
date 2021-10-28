from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class Skills(models.Model):
	title = models.CharField(max_length=50)

	def __str__(self):
		return f"{self.title}"

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
	photo_education = models.ImageField(
		upload_to='static/photo_education'
	)

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
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name_u = models.CharField(max_length=50, blank=False)
	last_name_u = models.CharField(max_length=50, blank=False)
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
		return f'{self.first_name_u}, {self.last_name_u}'

	class Meta:
		verbose_name = 'Аккаунт'
		verbose_name_plural = 'Аккаунты'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Chat(models.Model):
	DIALOG = 'D'
	CHAT = 'C'
	CHAT_TYPE_CHOICES = (
		(DIALOG, ('Dialog')),
		(CHAT, ('Chat'))
	)
	type_c = models.CharField(max_length=1, 
		choices=CHAT_TYPE_CHOICES, default=DIALOG)
	members = models.ManyToManyField(UserAccount)

	class Meta:
		verbose_name = 'Чат'
		verbose_name_plural = 'Чаты'

	def __str__(self):
		return f'{self.type_c}'


class Message(models.Model):
	chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
	author = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
	message = models.TextField()
	pub_date = models.DateTimeField(default=timezone.now)
	is_readed = models.BooleanField(default=False)

	class Meta:
		verbose_name = 'Сообщение'
		verbose_name_plural = 'Сообщения'
		ordering=['pub_date']

	def __str__(self):
		return f'{self.message}'