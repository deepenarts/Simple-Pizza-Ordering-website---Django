# Generated by Django 4.2 on 2023-06-06 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='uuid',
            new_name='uid',
        ),
        migrations.RenameField(
            model_name='cartitems',
            old_name='uuid',
            new_name='uid',
        ),
        migrations.RenameField(
            model_name='pizza',
            old_name='uuid',
            new_name='uid',
        ),
        migrations.RenameField(
            model_name='pizzacategory',
            old_name='uuid',
            new_name='uid',
        ),
    ]
