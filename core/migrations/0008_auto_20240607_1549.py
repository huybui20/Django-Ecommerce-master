# Generated by Django 2.2.4 on 2024-06-07 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200510_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='stock_no',
            field=models.IntegerField(),
        ),
    ]
