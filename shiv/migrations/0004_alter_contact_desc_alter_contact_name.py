# Generated by Django 4.1 on 2022-08-30 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shiv', '0003_alter_contact_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.TextField(max_length=222, null=b'I00\n'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=30, null=b'I00\n'),
        ),
    ]
