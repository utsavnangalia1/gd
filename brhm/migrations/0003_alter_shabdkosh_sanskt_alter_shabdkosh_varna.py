# Generated by Django 4.1 on 2022-09-05 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brhm', '0002_alter_shabdkosh_varna'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shabdkosh',
            name='sanskt',
            field=models.TextField(max_length=20, null=b'I00\n'),
        ),
        migrations.AlterField(
            model_name='shabdkosh',
            name='varna',
            field=models.CharField(max_length=10, null=b'I00\n'),
        ),
    ]
