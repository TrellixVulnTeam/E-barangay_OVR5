from rest_framework import serializers
from .models import Language
from django.contrib.auth import get_user_model

User = get_user_model()

class LanguageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Language
		fields = ('id','name','paradigm')