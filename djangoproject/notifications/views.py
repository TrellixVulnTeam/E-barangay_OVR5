from django.shortcuts import render
from .models import Send_notification
from django.contrib.auth.decorators import login_required


@login_required
def send_notification(request):
	return render(request,"send_notif.html")
