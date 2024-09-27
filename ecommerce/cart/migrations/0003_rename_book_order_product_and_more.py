# Generated by Django 5.1.1 on 2024-09-23 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_account_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='book',
            new_name='product',
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_status',
            field=models.CharField(default='pending', max_length=30),
        ),
    ]
