# Generated by Django 3.0.3 on 2020-04-27 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linea_base', '0004_auto_20200427_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineabase',
            name='estado',
            field=models.CharField(choices=[('Iniciado', 'Iniciado'), ('Pendiente', 'Pendiente')], default='Pendiente', max_length=12),
        ),
    ]
