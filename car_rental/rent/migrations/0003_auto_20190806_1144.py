# Generated by Django 2.2.3 on 2019-08-06 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0002_auto_20190802_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurance',
            name='insurance_number',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='rent',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rent', to='rent.Car'),
        ),
        migrations.AlterField(
            model_name='renteruser',
            name='PESEL',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='renteruser',
            name='driving_license_number',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]
