# Generated by Django 4.2.5 on 2024-01-05 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='bookings',
            new_name='booking',
        ),
        migrations.RenameModel(
            old_name='cleaners',
            new_name='cleaner',
        ),
        migrations.RenameModel(
            old_name='subscribers',
            new_name='subscriber',
        ),
    ]
