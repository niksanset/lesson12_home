# Generated by Django 4.2.7 on 2023-11-21 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_side', '0002_shop'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='shops',
            field=models.ManyToManyField(related_name='shops', to='shop_side.shop'),
        ),
    ]
