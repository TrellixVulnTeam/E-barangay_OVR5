from django.conf import settings
from django.db import models
from django.utils import timezone

User = settings.AUTH_USER_MODEL

CHOICES = [
	('Business Permit','Business Permit'),
	('Indigency','Indigency'),
	('Barangay Clearance','Barangay Clearance'),
	]

document = [
	('Received','Received'),
	('Pending','Pending'),
	('Did not received','Did not received'),
]

class Requested_document(models.Model):
	requested_document_sender	= models.ForeignKey(User,on_delete=models.CASCADE)
	type_of_document			= models.CharField(max_length=100, choices=CHOICES)
	purpose						= models.CharField(max_length=100)
	status_of_document			= models.CharField(max_length=100, choices=document)
	date_sent					= models.DateTimeField(default = timezone.now)

	def __str__(self):
		return self.type_of_document

complaint = [
	('Resolved','Resolved'),
	('Unresolved','Unresolved'),
	('Pending','Pending'),
]

class Complaint(models.Model):
	complaint_sender 			= models.ForeignKey(User,on_delete=models.CASCADE)
	complaint_description		= models.TextField(max_length=255)
	status_of_complaint			= models.CharField(max_length=100,choices=complaint)
	date_sent					= models.DateTimeField(default = timezone.now)

	def __str__(self):
		return self.complaint_description


class Suggestion(models.Model):
	suggestion_sender 		= models.ForeignKey(User,on_delete=models.CASCADE)
	suggestion_description	= models.TextField(max_length=255)
	date_sent				= models.DateTimeField(default= timezone.now)

	def __str__(self):
		return self.suggestion_description	