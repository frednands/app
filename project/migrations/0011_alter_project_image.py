# Generated by Django 5.0.4 on 2024-04-13 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, default='project/noimag.png', null=True, upload_to='project'),
        ),
    ]
