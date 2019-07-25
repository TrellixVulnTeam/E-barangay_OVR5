from django.conf import settings
from django.db import models
from django import forms
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager # the AbstractBaseUser is the class that gonna be implementing for user model
from django.core.validators import RegexValidator

User = settings.AUTH_USER_MODEL

class UserManager(BaseUserManager):
	# def create_user(self,username, email,password=None, is_active=True, is_staff=False, is_tanod=False, is_admin=False):
	def create_user(self,username,first_name,last_name,password=None, is_active=True, is_staff=False, is_tanod=False,
					 is_admin=False):
		# def create_user(self,username ,email,full_name ,gender=None ,password=None, is_active=True, is_staff=False, is_tanod=False, is_admin=False):
		if not username:
			raise ValueError("Users must have a username")		
		if not first_name:
			raise ValueError("Users must have a first name")
		if not last_name:
			raise ValueError("Users must have a last name")
		if not password:
			raise ValueError("Users must have a password")
		user = self.model(
			username = username,
			first_name = first_name,
			last_name = last_name
			)

			# USERNAME_FIELD = self.normalize_username(username)
			# username =  username
		# )	
		# email = self.model(
		# 	email = self.normalize_email(email)
		# 	)

		# user.first_name = first_name
		# user.last_name = last_name
		# user.gender = gender
		user.set_password(password) # change user password
		user.staff = is_staff
		user.tanod = is_tanod
		user.admin = is_admin
		user.active = is_active
		# user.user_type = user_power
		user.save(using=self._db)
		return user

	# def create_staffuser(self,username, email,full_name, gender, password=None):
	def create_staffuser(self,first_name,last_name, username, password=None,is_staff=True,is_tanod=False,is_admin=False):		
		user = self.model(
			username,
			first_name = first_name,
			last_name = last_name
			)
			# email,
			# full_name,
			# gender,
		user.set_password(password) # change user password
		user.staff = is_staff
		user.tanod = is_tanod
		user.admin = is_admin
		# user.user_type = user_power
		# is_tanod = True, # for the mean time, Change it to False if separating of keywords are already set up
		user.save(using=self._db)
		return user

	# def create_tanoduser(self,username, email,full_name, gender, password=None):
	def create_tanoduser(self,first_name,last_name, username, password=None,is_staff=False,is_tanod=True,is_admin=False):
		user = self.model(
				username = username,
				first_name = first_name,
				last_name = last_name
			)
		user.staff = is_staff
		user.tanod = is_tanod
		user.admin = is_admin
		# user.user_type = user_power
		user.set_password(password)
		user.save(using=self._db)
		return user
		# is_staff = True, # for the mean time, Change it to False if separating of keywords are already set up

	# def create_superuser(self,username, email,full_name, gender, password=None):
	def create_superuser(self,first_name,last_name, username, password,is_staff=True,is_tanod=True,is_admin=True):
		# user = self.create_superuser(
		# 	username,
		# 	password = password
		# 	# is_staff = True,
		# 	# is_tanod = True,
		# 	# is_admin = True
		# )
		user = self.model(
				username = username,
				first_name = first_name,
				last_name = last_name
				# password = password
			)
		# user.username
		user.staff = is_staff
		user.tanod = is_tanod
		user.admin = is_admin
		# user.user_type = user_power
		user.set_password(password)
		user.save(using=self._db)
		return user
		# def __str__(self):
		# 	return super(User, self).__str__()

# New user auth
sex = [
	(' Male','Male'),
	('Female','Female'),
]
userType = [
	('User','User'),
	('Staff','Staff'),
	('Tanod','Tanod'),
	('Chairman','Chairman'),
]
CHOICES=[('select1','select 1'),
     ('select2','select 2')]

# USERNAME_REGEX = '^[\w.@+-]+$'
# USERNAME_REGEX = '^\d{8}\-?(T|\d)\d{3}$'
USERNAME_REGEX = '^[a-zA-Z0-9]+$'
NAME_REGEX = '^[a-zA-Z]*$'
# NAME_REGEX = '[A-Z][a-zA-Z]$'
class User(AbstractBaseUser):
	# username 	=models.CharField(max_length=255, unique=True)
	username = models.CharField(
					max_length=150,
					validators = [
						RegexValidator(regex = USERNAME_REGEX,
										message = 'Username must be alphanumeric or contain numbers',
										code='invalid_username'
							)],
					unique=True
        )
	email		=models.EmailField(max_length = 255, unique=True,null=True)
	first_name 	=models.CharField(max_length=255, null=True, blank=False,
					validators = [RegexValidator(regex = NAME_REGEX,
									message = 'First name must be letters only',
									code = 'invalid_first_name'
					)]
		)
	last_name 	=models.CharField(max_length=255, null=True, blank=False,
					validators = [RegexValidator(regex = NAME_REGEX,
									message = 'Last name must be letters only',
									code = 'invalid_last_name'
					)]
		)
	# last_name 	=models.CharField(max_length=255, null=True, blank=False)
	# user_type	=models.BooleanField(default='user_power',null=False)
	gender		=models.CharField(max_length=100,choices=sex,null=False)
	# user_type	=models.CharField(max_length=100,choices=userType,null=False)
	active		=models.BooleanField(default=True) # can login or regular user
	staff		=models.BooleanField(default=False) # non-super user
	tanod		=models.BooleanField(default=False) # non-super user
	admin		=models.BooleanField(default=False) # superuser
	date_joined	=models.DateTimeField(auto_now=False, auto_now_add=True)

	USERNAME_FIELD = 'username' #username
	# USERNAME_FIELD and password are required by default
	REQUIRED_FIELDS = ['first_name','last_name']	#['username','email,','first_name','last_name'] #sample ['full_name']

	objects = UserManager()

	def __str__(self):
		return self.username

	def get_full_name(self):
		return self.username

	def get_first_name(self):
		if first_name:
			return self.first_name
		return self.username

	def get_last_name(self):
		if last_name:
			return self.last_name
		return self.username

	def get_short_name(self):
		return self.username

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	@property
	def is_staff(self):
		return self.staff

	@property
	def is_tanod(self):
		return self.tanod

	@property
	def is_admin(self):
		return self.admin

	@property
	def is_active(self):
		return self.active

# class AdminUser(User):
# 	admin = True