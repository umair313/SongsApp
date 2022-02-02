# Generated by Django 4.0.1 on 2022-01-31 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_alter_track_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='tracks',
            field=models.ManyToManyField(through='songs.PlaylistTrack', to='songs.Track'),
        ),
    ]
