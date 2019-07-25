from django.contrib import admin
from django import forms
# from .models import User
# from django.db import models
from .models import User
# from models.UserManager import create_user
# from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
# from .models import create_staffuser,create_tanoduser,create_user,create_superuser,is_staff

# User = get_user_model()

class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','gender')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username','password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

sex = [
    (' Male','Male'),
    ('Female','Female'),
]

# class UserRegistration(forms.ModelForm):
#     """
#     A form that creates a user, with no privileges, from the given username and
#     password.
#     """
#     error_messages = {
#         'password_mismatch': _("The two password fields didn't match."),
#     }
#     password1 = forms.CharField(
#         label=_("Password"),
#         strip=False,
#         widget=forms.PasswordInput,
#         help_text=password_validation.password_validators_help_text_html(),
#     )
#     password2 = forms.CharField(
#         label=_("Password confirmation"),
#         widget=forms.PasswordInput,
#         strip=False,
#         help_text=_("Enter the same password as before, for verification."),
#     )

#     class Meta:
#         model = User
#         fields = ("username",)
#         field_classes = {'username': UsernameField}

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if self._meta.model.USERNAME_FIELD in self.fields:
#             self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update({'autofocus': True})

#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError(
#                 self.error_messages['password_mismatch'],
#                 code='password_mismatch',
#             )
#         return password2

#     def _post_clean(self):
#         super()._post_clean()
#         # Validate the password after self.instance is updated with form data
#         # by super().
#         password = self.cleaned_data.get('password2')
#         if password:
#             try:
#                 password_validation.validate_password(password, self.instance)
#             except forms.ValidationError as error:
#                 self.add_error('password2', error)

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user

class RegistrationForm(UserCreationForm):
    # staff       = models.BooleanField(default=True)
    email       = forms.EmailField(required=True)
    # gender = forms.ChoiceField(choices=sex, widget=forms.RadioSelect,required=True)#it change the list down to radio select
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','gender','email','password1','password2']

    def save(self, commit=True): # commit - it means like you're telling the system to go ahead save it to the database
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name'] #cleaned_data used to avoid sql injection
        user.last_name  = self.cleaned_data['last_name']
        user.email      = self.cleaned_data['email']

        if commit:
            user.save()
        return user

# class UserAdmin(admin.ModelAdmin):

# class RegisterForm(forms.ModelForm):
#     first_name  = forms.CharField(max_length=255)
#     last_name   = forms.CharField(max_length=255)
#     password1   = forms.CharField(widget=forms.PasswordInput)
#     password2   = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)


#     class Meta:
#         model = User
#         fields = ('username','first_name','last_name','gender','email','password1','password2')

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     qs = User.objects.filter(username=usernmae)
    #     if qs.exists():
    #         raise forms.ValidationError("username is taken")
    #     return username

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     qs = User.objects.filter(email=email)
    #     if qs.exists():
    #         raise forms.ValidationError("email is taken")
    #     return email

    # def clean_password2(self):
    #     # Check that the two password entries match
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("Passwords don't match")
    #     return password2

class StaffRegisterForm(UserCreationForm):
    sex = [
        (' Male','Male'),
        ('Female','Female'),
    ]
    email = forms.EmailField()
    is_staff = True
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    gender = forms.CharField(max_length=255)

    class Meta:
    # fullname = first_name + last_name
        model = User
        fields = ['username','gender','first_name','last_name','email','password1','password2']

# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username','email','first_name','last_name']

# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields =['image']