# Generated by Django 3.2.3 on 2021-05-20 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
