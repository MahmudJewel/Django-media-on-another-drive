# Generated by Django 4.1.2 on 2022-10-26 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinfo',
            name='img',
            field=models.ImageField(default='product/default.png', upload_to='product/'),
        ),
    ]
