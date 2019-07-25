from django.contrib import admin
from django import forms
from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import RegexValidator
# from .custom_user.models import User
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

User = get_user_model()
sex=[('Male','Male'),
         ('Female','Female')]
USERNAME_REGEX = '^[a-zA-Z0-9]+$'
NAME_REGEX = '^[a-zA-Z]*$'
class UserRegisterForm(UserCreationForm):

	email = forms.EmailField()
	first_name = forms.CharField(max_length=255)
	# first_name = forms.CharField(max_length=255,
	# 				validators = [RegexValidator(regex = NAME_REGEX,
	# 								message = 'First name must be letters only',
	# 								code = 'invalid_first_name'
	# 				)]
	# 	)
	last_name = forms.CharField(max_length=255)
	# last_name = forms.CharField(max_length=255,
	# 				validators = [RegexValidator(regex = NAME_REGEX,
	# 								message = 'Last name must be letters only',
	# 								code = 'invalid_last_name'
	# 				)]
	# 	)

    # gender 	= forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
	# gender = models.CharField(max_length=255,choices=sex)
	# gender = forms.CharField(max_length=100,choices = genderType)
	# user_type = forms.CharField(max_length=100, choices=choices)
	class Meta:
		# fullname = first_name + last_name
		model = User
		fields = ['username','first_name','last_name','email','password1','password2','gender']
# class UserAdmin(admin.ModelAdmin):
# 	list_display = ['username','gender','first_name','last_name','email']
# admin.site.register(UserRegisterForm,UserAdmin)


class UserUpdateForm(forms.ModelForm):
	# email = forms.EmailField()
	# gender = forms.ChoiceField(choices=sex, widget=forms.RadioSelect())
	class Meta:
		model = User
		fields = ['username','email','gender','first_name','last_name']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields =['image']