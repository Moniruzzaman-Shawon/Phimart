# Generated by Django 5.2.4 on 2025-07-30 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_cart_id'),
        ('product', '0003_review'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={('cart', 'product')},
        ),
    ]
