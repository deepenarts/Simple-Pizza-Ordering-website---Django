# Generated by Django 4.2 on 2023-06-06 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_uuid_cart_uid_rename_uuid_cartitems_uid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitems',
            old_name='Pizza',
            new_name='pizza',
        ),
    ]
