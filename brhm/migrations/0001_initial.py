# Generated by Django 4.1 on 2022-09-05 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shabdkosh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('varna', models.CharField(max_length=10, null=b'I00\n')),
                ('meaning', models.TextField(max_length=100, null=b'I00\n')),
                ('sanskt', models.CharField(max_length=20, null=b'I00\n')),
                ('eng', models.CharField(max_length=15, null=b'I00\n')),
                ('category', models.CharField(max_length=15)),
            ],
        ),
    ]
