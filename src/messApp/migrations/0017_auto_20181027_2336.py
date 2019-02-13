# Generated by Django 2.1.2 on 2018-10-27 17:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('messApp', '0016_meal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='item',
        ),
        migrations.AddField(
            model_name='meal',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
