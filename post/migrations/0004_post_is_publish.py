# Generated by Django 5.0.4 on 2024-04-26 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_rename_update_at_post_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_publish',
            field=models.BooleanField(default=False),
        ),
    ]
