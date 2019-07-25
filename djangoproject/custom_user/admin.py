from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm,UserAdminChangeForm

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username','email','first_name','last_name','gender',
                    'active','staff','tanod','admin')
    list_filter = ('admin','staff','tanod','active') # can be date joined
    fieldsets = (
        (None, {'fields': ('username','email', 'password')}),
        ('Personal info', {'fields': ('first_name','last_name','gender',)}),
        ('Permissions', {'fields': ('admin','staff','tanod','active',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email','first_name',
                        'last_name','gender', 'password1', 'password2')}
        ),
    )
    search_fields = ('first_name','last_name','username')
    ordering = ('username',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
# class UserAdmin(admin.ModelAdmin):

# 	search_fields = ['first_name','last_name']
# 	form = UserAdminChangeForm #update view
# 	add_form = UserAdminCreationForm # create view
# 	# class Meta:
# 	# 	model = User

# 	list_display = ['username','email','first_name','last_name',
# 		'gender','admin','tanod','staff','active','date_joined'
# 	]
# 	list_filter = ['date_joined'] # for filtering updates of post
# admin.site.register(User,UserAdmin)

# admin.site.register(User)
