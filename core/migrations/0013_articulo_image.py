# Generated by Django 2.1.5 on 2019-09-22 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_pedido_direccion_envio'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
