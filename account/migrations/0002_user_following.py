# Generated by Django 4.0.1 on 2022-01-31 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0005_track_playlists_alter_playlisttrack_playlist_and_more'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(to='songs.Artist'),
        ),
    ]
