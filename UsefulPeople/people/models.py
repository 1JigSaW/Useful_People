from django.db import models

class Users(models.Model):
	login = models.CharField(max_length=50, blank=False)
	email = models.CharField(max_length=50, blank=False)
	password = models.CharField(max_length=20, blank=False)
