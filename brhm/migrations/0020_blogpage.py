# Generated by Django 4.1 on 2022-10-03 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brhm', '0019_delete_blogpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtag', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=1000)),
                ('img', models.ImageField(max_length=30, upload_to='')),
                ('link', models.TextField(max_length=20)),
                ('read_time', models.CharField(max_length=20)),
                ('author_name', models.CharField(max_length=40)),
            ],
        ),
    ]
