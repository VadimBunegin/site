# Generated by Django 4.0.1 on 2022-09-27 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0003_calchistory_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calchistory',
            name='author',
        ),
    ]
