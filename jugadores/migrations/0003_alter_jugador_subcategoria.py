# Generated by Django 5.1.6 on 2025-03-05 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jugadores', '0002_jugador_categoria_jugador_imagen_jugador_p_apellido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='subcategoria',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], default='BEN', max_length=6),
        ),
    ]
