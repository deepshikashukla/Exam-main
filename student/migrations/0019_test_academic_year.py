# Generated by Django 3.0.5 on 2021-02-22 07:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0018_auto_20210221_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='Academic_year',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]