# Generated by Django 5.0.3 on 2024-03-05 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSetFile',
            fields=[
                ('id',
                 models.BigAutoField(auto_created=True,
                                     primary_key=True,
                                     serialize=False,
                                     verbose_name='ID')),
                ('File', models.FileField(upload_to='Excel/')),
            ],
            options={
                'verbose_name': 'DataSetFile',
                'verbose_name_plural': 'DataSetFiles',
            },
        ),
    ]
