# Generated by Django 2.1.7 on 2019-03-04 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='lon',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
