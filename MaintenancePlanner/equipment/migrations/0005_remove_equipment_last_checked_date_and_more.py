# Generated by Django 4.2.3 on 2023-07-18 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0004_alter_equipment_year_of_manufacture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='last_checked_date',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='next_check_date',
        ),
    ]