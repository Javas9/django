# Generated by Django 3.2.2 on 2021-05-13 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_at', models.TimeField(auto_now_add=True)),
                ('upload_at', models.TimeField(auto_now=True)),
                ('photo', models.ImageField(upload_to='photo/%y/%m/%d/')),
                ('in_publisher', models.BooleanField(default=True)),
            ],
        ),
    ]
