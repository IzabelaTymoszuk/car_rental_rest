# Generated by Django 2.2.3 on 2019-08-02 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rent',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='rent',
            name='number_of_day',
        ),
        migrations.AlterField(
            model_name='car',
            name='VIN',
            field=models.CharField(max_length=17, unique=True),
        ),
    ]
