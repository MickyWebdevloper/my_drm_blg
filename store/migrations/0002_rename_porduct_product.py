# Generated by Django 4.0.4 on 2022-08-21 10:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Porduct',
            new_name='Product',
        ),
    ]
