# Generated by Django 4.1.2 on 2022-11-01 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_shipping'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shipping',
            old_name='address',
            new_name='delivery_address',
        ),
        migrations.AddField(
            model_name='shipping',
            name='billing_address',
            field=models.CharField(default='a', max_length=250),
        ),
    ]
