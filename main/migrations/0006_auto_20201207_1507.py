# Generated by Django 2.2.17 on 2020-12-07 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_casa_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casa',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
