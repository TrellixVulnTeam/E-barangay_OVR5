from django.shortcuts import render
from .models import Send_notification
from django.contrib.auth.decorators import login_required
@login_required
def send_notification(request):
    if request.method == 'POST':    
        find_user = request.POST.get('username')
        content = request.POST.get('content')
        current_user = request.user
        print(find_user,content,current_user)
    return render(request,"send_notif.html")

