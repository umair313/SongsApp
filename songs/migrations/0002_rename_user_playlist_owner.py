# Generated by Django 4.0.1 on 2022-01-31 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playlist',
            old_name='user',
            new_name='owner',
        ),
    ]
