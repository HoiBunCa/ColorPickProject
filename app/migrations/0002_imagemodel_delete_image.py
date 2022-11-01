# Generated by Django 4.1.2 on 2022-10-31 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('image', models.FileField(upload_to='images/')),
                ('user', models.TextField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]