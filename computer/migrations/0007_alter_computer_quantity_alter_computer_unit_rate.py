# Generated by Django 4.1.4 on 2022-12-20 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0006_alter_computer_computer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='computer',
            name='unit_rate',
            field=models.PositiveIntegerField(),
        ),
    ]
