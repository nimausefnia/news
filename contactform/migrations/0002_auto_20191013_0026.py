# Generated by Django 2.2.5 on 2019-10-12 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='date',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AddField(
            model_name='contactform',
            name='time',
            field=models.CharField(default='', max_length=12),
        ),
    ]
