# Generated by Django 3.2.3 on 2021-05-24 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ninja_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dojo',
            name='City',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='dojo',
            name='State',
            field=models.CharField(max_length=255),
        ),
    ]
