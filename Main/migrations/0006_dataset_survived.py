# Generated by Django 5.0.3 on 2024-03-05 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_remove_singletonmodel_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='Survived',
            field=models.IntegerField(default=0),
        ),
    ]