# Generated by Django 4.1.3 on 2022-11-04 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='avi', max_length=255, unique=True),
        ),
    ]
