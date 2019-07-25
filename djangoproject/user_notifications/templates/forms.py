from django import forms
from .models import user_notifications
from django.contrib.auth import get_user_model

User = get_user_model()

class NotificationForm(forms.ModelForm):
	pass
