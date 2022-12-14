# Generated by Django 4.1 on 2022-09-12 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brhm', '0012_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shabdkosh',
            name='eng',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='shabdkosh',
            name='meaning',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='shabdkosh',
            name='sanskt',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='shabdkosh',
            name='varna',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='varnamala',
            name='angala',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='varnamala',
            name='chakra',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='varnamala',
            name='varn',
            field=models.CharField(max_length=5),
        ),
    ]
