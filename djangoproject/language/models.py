from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Language(models.Model):
    name = models.CharField(max_length=50)
    paradigm = models.CharField(max_length=50)

    def __str__(self):
        return self.name