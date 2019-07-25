from django.conf import settings
from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import (
# 	AbstractBaseUser # the AbstractBaseUser is the class that gonna be implementing for user model
# )
User = get_user_model()
# User = settings.AUTH_USER_MODEL # this should be apply at all models per apps

from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete =models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	update = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		super(Profile,self).save(*args, **kwargs)
	#def save(self):
		#super().save()
	# def save(self, *args, **kwargs):
    	

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)
