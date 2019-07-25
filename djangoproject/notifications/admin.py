from django.contrib import admin
from .models import Send_notification
from django.conf import settings
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .forms import UserAdminCreationForm,UserAdminChangeForm
# from .models import User

User = settings.AUTH_USER_MODEL

# class NotifAdmin(BaseUserAdmin):
class Send_NotifAdmin(admin.ModelAdmin):
	# search_fields = ['title']
	list_display = ['sender','notification_concern','content','date_sent']
	# list_filter = ['date_sent'] # for filtering updates of post
	# class Meta:
 #    	model = User

    # ordering = ('username')
    # filter_horizontal = ()


# class Send_NotifAdmin(BaseUserAdmin):
#     # The forms to add and change user instances
#     # form = UserAdminChangeForm
#     # add_form = UserAdminCreationForm

#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     list_display = ('username','notification_concern','last_contentname','date_sent')
#     list_filter = ('date_sent') # can be date joined
#     search_fields = ('first_name','last_name')
#     ordering = ('username',)
#     filter_horizontal = ()

admin.site.register(Send_notification, Send_NotifAdmin)

