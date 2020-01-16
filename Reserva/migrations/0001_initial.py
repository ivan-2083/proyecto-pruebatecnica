# Generated by Django 2.1.15 on 2020-01-15 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mae_sala',
            fields=[
                ('msl_id', models.AutoField(primary_key=True, serialize=False)),
                ('msl_nombre', models.CharField(max_length=100)),
                ('msl_numero', models.CharField(max_length=3)),
                ('msl_activa', models.BooleanField(default=True)),
                ('msl_descripción', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='nub_arrendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nrr_nombre_sala', models.CharField(max_length=100)),
                ('nrr_nombre_comuna', models.CharField(max_length=100)),
                ('nrr_nombre_region', models.CharField(max_length=100)),
                ('nrr_fecha', models.DateField()),
                ('nrr_hora', models.TimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ref_comuna',
            fields=[
                ('rcm_id', models.AutoField(primary_key=True, serialize=False)),
                ('rcm_nombre', models.CharField(max_length=100)),
                ('rcm_id_regiones', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ref_region',
            fields=[
                ('rrg_id', models.AutoField(primary_key=True, serialize=False)),
                ('rrg_nombre', models.CharField(max_length=100)),
                ('rrg_ordinal', models.CharField(max_length=100)),
            ],
        ),
    ]
