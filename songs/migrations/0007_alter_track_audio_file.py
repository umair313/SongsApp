# Generated by Django 4.0.1 on 2022-02-01 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0006_track_audio_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='audio_file',
            field=models.FileField(upload_to='tracks'),
        ),
    ]
