# Generated by Django 3.2.3 on 2021-05-26 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice_app', '0002_rename_passwd_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auther',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('notes', models.TextField(default='Author notes')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='auther',
            name='books',
            field=models.ManyToManyField(related_name='author', to='practice_app.Book'),
        ),
    ]