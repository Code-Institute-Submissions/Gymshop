# Generated by Django 3.1.5 on 2021-02-14 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210130_1317'),
        ('wishlist', '0004_auto_20210214_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='wished_item',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='wished_item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
            preserve_default=False,
        ),
    ]
