# Generated by Django 2.2 on 2023-10-21 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staticapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='travelspots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=250)),
                ('timg', models.ImageField(upload_to='images')),
                ('det', models.TextField()),
            ],
        ),
    ]
