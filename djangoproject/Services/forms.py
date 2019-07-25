from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from models import Requested_document

class StaffDocumentForm(Requested_document):

	class Meta:
		model = User
		fields= ['username','Type_of_document','Purpose','date_sent']

	# def __str__(self):
	# 	return self.Type_of_document