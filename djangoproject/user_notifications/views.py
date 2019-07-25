from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import UserNotification
from django.db import models

User = get_user_model()

@login_required
def user_notifications(request):
	context = {
		'notifications':UserNotification.objects.all()
	}
	return render(request,'notification.html',context)

def get_queryset(self):
	user = get_object_or_404(User,username=self.kwargs.get('username'))
	return Post.objects.filter(author=user).order_by('-date_posted')

