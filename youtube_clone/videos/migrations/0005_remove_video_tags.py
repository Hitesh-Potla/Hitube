from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_alter_video_channel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='tags',
        ),
    ]
