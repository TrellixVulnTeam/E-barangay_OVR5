from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from custom_user.forms import StaffRegisterForm,RegistrationForm
from .models import User,UserManager

# User = get_user_model()

@login_required
def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			#form.save()
			username = form.cleaned_data.get('username')
			form.save()
			messages.success(request, f'{ username } added successfully ')
			return redirect('home')
	else:
		form = RegistrationForm()
	return render(request, 'user_registration.html' ,{'form': form})

@login_required
def register_staff(request):
	if request.method == 'POST':
		form = StaffRegisterForm(request.POST)
		if form.is_valid():
			#form.save()
			username = form.cleaned_data.get('username')
			form.save()
			messages.success(request, f'{ username } added successfully ')
			return redirect('home')
	else:
		form = StaffRegisterForm()
	return render(request, 'register.html' ,{'form': form})
