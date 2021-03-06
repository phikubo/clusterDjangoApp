# Generated by Django 2.0.2 on 2018-09-05 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area_local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ubicacion', models.PositiveSmallIntegerField()),
                ('coordenadas', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Centro_comercial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_centro', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Combos_promos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='Mi primer combo', max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('compros', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clienteapp.Area_local')),
            ],
        ),
        migrations.AddField(
            model_name='area_local',
            name='inscripcion_cc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clienteapp.Centro_comercial'),
        ),
    ]
