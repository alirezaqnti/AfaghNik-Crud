# Generated by Django 5.0.3 on 2024-03-05 07:13

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_datasetfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasetfile',
            name='Created',
            field=models.DateTimeField(auto_now_add=True,
                                       default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datasetfile',
            name='Modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
