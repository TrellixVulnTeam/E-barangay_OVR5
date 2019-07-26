from django.shortcuts import render
from .models import Send_notification
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver

global qwe
qwe = "haha"

@receiver(post_save, sender=Send_notification)
def callback(sender, **kwargs):
    print("hehehe")
    global qwe
    qwe = "Notified!"

@login_required
def send_notification(request):
    if request.method == 'POST':    
        find_user = request.POST.get('username')
        content = request.POST.get('content')
        current_user = request.user
        Send_notification.objects.create(content = content, sender=current_user)
        print(find_user,content,current_user)
    return render(request,"send_notif.html",{'output':qwe})

