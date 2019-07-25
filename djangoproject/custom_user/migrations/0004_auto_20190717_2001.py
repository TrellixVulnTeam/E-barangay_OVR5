# Generated by Django 2.1.7 on 2019-07-17 12:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0003_auto_20190717_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=255, null=True, validators=[django.core.validators.RegexValidator(code='invalid_first_name', message='First name must be letters only', regex='^[a-zA-Z]*$')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=255, null=True, validators=[django.core.validators.RegexValidator(code='invalid_last_name', message='Last name must be letters only', regex='^[a-zA-Z]*$')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=300, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Username must be alphanumeric or contain numbers', regex='^[a-zA-Z0-9]+$')]),
        ),
    ]
