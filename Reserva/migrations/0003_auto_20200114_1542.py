# Generated by Django 2.1.15 on 2020-01-14 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reserva', '0002_Reserva'),
    ]

    operations = [
        migrations.AddField(
            model_name='nub_arrendar',
            name='nrr_hora',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='nub_arrendar',
            name='nrr_fecha',
            field=models.DateField(),
        ),
    ]
