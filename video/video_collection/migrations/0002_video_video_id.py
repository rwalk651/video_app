# Generated by Django 5.1.3 on 2024-11-27 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_collection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video_id',
            field=models.CharField(default=1, max_length=40, unique=True),
            preserve_default=False,
        ),
    ]
