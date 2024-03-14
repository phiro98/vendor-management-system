# Generated by Django 5.0.3 on 2024-03-14 06:43

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('VendorProfileManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalPerformance',
            fields=[
                ('p_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('on_time_delivery_rate', models.FloatField(blank=True, default=None, null=True)),
                ('quality_rating_avg', models.FloatField(blank=True, default=None, null=True)),
                ('average_response_time', models.FloatField(blank=True, default=None, null=True)),
                ('fulfillment_rate', models.FloatField(blank=True, default=None, null=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VendorProfileManagement.vendor')),
            ],
            options={
                'db_table': 'historical_performance',
            },
        ),
    ]
