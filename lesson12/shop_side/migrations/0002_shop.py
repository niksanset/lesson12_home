# Generated by Django 4.2.7 on 2023-11-21 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_side', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('adress', models.CharField(max_length=255)),
            ],
        ),
    ]