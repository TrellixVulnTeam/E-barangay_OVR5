from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
	display_list = ['user','update']

admin.site.register(Profile,ProfileAdmin)
