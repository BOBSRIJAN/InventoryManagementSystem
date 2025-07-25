# Generated by Django 5.2.3 on 2025-07-21 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('userid', models.BigIntegerField()),
                ('quantity', models.IntegerField()),
                ('category', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('isInMarketPlaces', models.BooleanField(null=True)),
                ('description', models.TextField(max_length=1000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='item_images/')),
                ('ItemCondition', models.IntegerField(null=True)),
                ('isExpired', models.BooleanField(default=False)),
                ('isAvailable', models.BooleanField(default=True)),
                ('isSold', models.BooleanField(default=False)),
                ('add_date', models.CharField(max_length=50, null=True)),
                ('exp_date', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
