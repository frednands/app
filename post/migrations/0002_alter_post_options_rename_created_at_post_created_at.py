# Generated by Django 5.0.4 on 2024-04-26 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'managed': True, 'ordering': ['-created_at'], 'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Created_at',
            new_name='created_at',
        ),
    ]
