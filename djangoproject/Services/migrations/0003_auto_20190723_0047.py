# Generated by Django 2.1.7 on 2019-07-22 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0002_auto_20190723_0045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='status_complaint',
            new_name='status_of_complaint',
        ),
        migrations.RenameField(
            model_name='requested_document',
            old_name='status',
            new_name='status_of_document',
        ),
    ]
