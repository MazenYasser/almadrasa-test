# Generated by Django 5.0.4 on 2024-04-27 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0004_alter_subject_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='image',
            field=models.ImageField(blank=True, max_length=1024, null=True, upload_to='subjects/'),
        ),
    ]
