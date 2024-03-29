# Generated by Django 5.0.3 on 2024-03-14 06:43

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('vendor_code', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('contact_details', models.CharField(max_length=20, unique=True)),
                ('address', models.CharField(max_length=3000)),
                ('on_time_delivery_rate', models.FloatField(blank=True, default=None, null=True)),
                ('quality_rating_avg', models.FloatField(blank=True, default=None, null=True)),
                ('average_response_time', models.FloatField(blank=True, default=None, null=True)),
                ('fulfillment_rate', models.FloatField(blank=True, default=None, null=True)),
            ],
            options={
                'db_table': 'vendor',
            },
        ),
    ]
