# Generated by Django 3.2.9 on 2022-02-17 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0006_auto_20220217_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kategoria',
            name='Podkategoria',
        ),
        migrations.AddField(
            model_name='kategoria',
            name='podkategoria',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.DeleteModel(
            name='Podkategoria',
        ),
    ]
