# Generated by Django 4.0.4 on 2022-06-26 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gardens', '0006_alter_garden_is_temi_ready_alter_garden_is_water'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garden',
            name='is_turn_on',
            field=models.IntegerField(default=0),
        ),
    ]
