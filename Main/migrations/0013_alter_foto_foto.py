# Generated by Django 3.2.9 on 2022-02-22 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0012_alter_foto_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='foto',
            field=models.ImageField(upload_to='images/'),
        ),
    ]