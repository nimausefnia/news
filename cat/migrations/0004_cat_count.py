# Generated by Django 2.2.5 on 2019-10-08 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0003_remove_cat_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
