# Generated by Django 4.1 on 2022-09-29 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brhm', '0016_shabdkosh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shabdkosh',
            name='gramgp',
            field=models.CharField(max_length=50),
        ),
    ]