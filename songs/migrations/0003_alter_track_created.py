# Generated by Django 4.0.1 on 2022-01-31 11:42

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_rename_user_playlist_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created'),
        ),
    ]