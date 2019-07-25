from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL

CHOICES = [
	('Requested Document','Requested Document'),
	('Complaint','Complaint')
]
class UserNotification(models.Model):
	sender			= models.ForeignKey(User,on_delete=models.CASCADE)
	concern_type	= models.CharField(max_length=100,choices=CHOICES)
	content			= models.TextField(max_length=255,blank=False)
	date_sent		= models.DateTimeField(default = timezone.now)

	def __str__(self):
		return self.concern_type