# Generated by Django 4.1.1 on 2022-09-23 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='appname')),
                ('region', models.CharField(max_length=20)),
                ('created_date', models.DateTimeField()),
            ],
        ),
    ]
