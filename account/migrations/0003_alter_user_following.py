# Generated by Django 4.0.1 on 2022-02-07 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0008_remove_track_playlists'),
        ('account', '0002_user_following'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(related_name='followers', to='songs.Artist'),
        ),
    ]
