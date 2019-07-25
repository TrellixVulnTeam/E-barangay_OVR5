from django.contrib import admin
# from django.contrib.auth.models import Group
from .models import Post

# admin.site.unregister(Group)#This is the default of django if necessary just register it again or delete because it's default :p

# class PostAdmin(admin.ModelAdmin):
# 	search_fields = ['author']
# 	list_display = ['title','content','author','date_posted']
# 	list_filter = ['date_posted'] # for filtering updates of post
class PostAdmin(admin.ModelAdmin):
    # The forms to add and change user instances
    # form = UserAdminChangeForm
    # add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('title','content','author','date_posted',)
    list_filter = ('date_posted',) # can be date joined
    search_fields = ('author',)
    filter_horizontal = ()
# class Send_NotifAdmin(admin.ModelAdmin):
# 	list_display = ['search','notification_concern','content','date_sent']
# 	list_filter = ['date_sent'] # for filtering updates of notif
admin.site.register(Post,PostAdmin)
# admin.site.register(Send_notification,Send_NotifAdmin)
