# Generated by Django 4.1.7 on 2023-03-11 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("first", "0006_alter_calchistory_date_alter_calchistory_first_and_more"),
    ]

    operations = [
        migrations.RenameModel(old_name="CalcHistory", new_name="History",),
    ]
