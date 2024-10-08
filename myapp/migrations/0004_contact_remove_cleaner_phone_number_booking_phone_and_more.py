# Generated by Django 4.2.5 on 2024-01-09 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_booking_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fill_name', models.CharField(max_length=200)),
                ('phone', models.IntegerField(null=True)),
                ('email_address', models.CharField(max_length=200)),
                ('comments', models.TextField(max_length=2000)),
            ],
        ),
        migrations.RemoveField(
            model_name='cleaner',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='booking',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='cleaner',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
