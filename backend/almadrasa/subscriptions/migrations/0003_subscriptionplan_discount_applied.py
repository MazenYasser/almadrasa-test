# Generated by Django 5.0.4 on 2024-04-25 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptionplan',
            name='discount_applied',
            field=models.BooleanField(default=False),
        ),
    ]