# Generated by Django 4.1 on 2022-10-09 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brhm', '0032_rename_topic_strotam_strota'),
    ]

    operations = [
        migrations.CreateModel(
            name='shlokas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shloka', models.CharField(max_length=50)),
                ('shlokahead', models.CharField(max_length=50)),
                ('shlksnskt', models.CharField(max_length=500)),
                ('shlkengconv', models.TextField(max_length=500)),
                ('shlkengmean', models.TextField(max_length=500)),
            ],
        ),
    ]
