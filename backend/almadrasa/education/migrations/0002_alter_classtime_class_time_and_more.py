# Generated by Django 5.0.4 on 2024-04-25 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classtime',
            name='class_time',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='weeklyclasscount',
            name='weekly_count',
            field=models.CharField(max_length=128),
        ),
    ]
