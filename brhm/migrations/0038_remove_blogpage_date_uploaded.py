# Generated by Django 4.1 on 2022-10-12 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brhm', '0037_blogpage_date_uploaded'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='date_uploaded',
        ),
    ]
