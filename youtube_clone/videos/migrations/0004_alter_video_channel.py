# Generated by Django 5.1.4 on 2025-01-23 06:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_tag_video_category_video_is_liked_video_likes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.channel'),
        ),
    ]
