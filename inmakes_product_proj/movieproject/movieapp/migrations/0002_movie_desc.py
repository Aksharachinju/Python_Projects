# Generated by Django 2.2 on 2023-11-01 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='desc',
            field=models.TextField(default='trty'),
            preserve_default=False,
        ),
    ]