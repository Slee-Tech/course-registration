# Generated by Django 2.2.6 on 2019-11-04 01:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='enrollee',
            field=models.ManyToManyField(blank=True, related_name='student', to=settings.AUTH_USER_MODEL),
        ),
    ]
