# Generated by Django 3.0.5 on 2020-04-17 09:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminpanel', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Challenge',
            new_name='Practice',
        ),
    ]
