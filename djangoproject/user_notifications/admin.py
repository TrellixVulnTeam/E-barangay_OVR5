from django.contrib import admin
from .models import UserNotification

class AdminUserNotification(admin.ModelAdmin):
	list_display 	= ['sender','concern_type','content','date_sent']
	list_filter 	= ['date_sent']

admin.site.register(UserNotification,AdminUserNotification)