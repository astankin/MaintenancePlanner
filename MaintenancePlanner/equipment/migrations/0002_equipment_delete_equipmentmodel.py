# Generated by Django 4.2.3 on 2023-07-03 16:03

import MaintenancePlanner.equipment.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0002_alter_plant_country'),
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=30, validators=[MaintenancePlanner.equipment.validators.equipment_name_validator])),
                ('type', models.CharField(choices=[('Machine', 'Machine'), ('Measuring tool', 'Measuring tool'), ('Mand power tool', 'Hand power tool')], max_length=30)),
                ('acquisition_date', models.DateField(blank=True, null=True, verbose_name='Acquisition Date')),
                ('acquisition_value', models.FloatField(blank=True, null=True, verbose_name='Acquisition Value')),
                ('currency_code', models.CharField(choices=[('EUR', 'EUR'), ('BGN', 'BGN'), ('USD', 'USD')], default='EUR', max_length=10)),
                ('manufacturer', models.CharField(blank=True, max_length=30, null=True)),
                ('model_number', models.CharField(blank=True, max_length=30, null=True, verbose_name='Model Number')),
                ('part_number', models.CharField(blank=True, max_length=30, null=True, verbose_name='Manufacturer Part Number')),
                ('serial_number', models.CharField(blank=True, max_length=30, null=True, verbose_name='Manufacturer Serial Number')),
                ('last_checked_date', models.DateField(blank=True, null=True, verbose_name='Last Checked Date')),
                ('next_check_date', models.DateField(blank=True, null=True, verbose_name='Next Check Date')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plant.department')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plant.plant')),
            ],
        ),
        migrations.DeleteModel(
            name='EquipmentModel',
        ),
    ]
