# Generated by Django 4.2.11 on 2024-04-02 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Panaderia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=250)),
                ('anyo_fundacion', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Panadero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('apellidos', models.CharField(max_length=150)),
                ('fecha_nacimiento', models.DateField()),
                ('panaderia', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='panaderiaCurroApp.panaderia')),
            ],
        ),
    ]
