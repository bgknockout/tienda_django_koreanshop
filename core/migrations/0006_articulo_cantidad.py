# Generated by Django 2.1.5 on 2019-09-20 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_articulo_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='cantidad',
            field=models.IntegerField(default=1),
        ),
    ]
