from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

User = settings.AUTH_USER_MODEL
concern_choices = [
	('Requested Document','Requested Document'),
	('Complaint','Complaint'),
	]
class Send_notification(models.Model):
	# user_reciever = models.ForeignKey(User,max_length=100,on_delete =models.CASCADE)
	# title = models.CharField(max_length=100)
	notification_concern 	= models.CharField(max_length=100,choices=concern_choices)
	content 			 	= models.TextField(max_length=255)
	date_sent				= models.DateTimeField(default = timezone.now)
	sender					= models.ForeignKey(User,on_delete=models.CASCADE) # sender to user
	
	def __str__(self):
		return self.notification_concern

	# def get_absolute_url(self):
	# 	return reverse('post-detail', kwargs={'pk':self.pk})
