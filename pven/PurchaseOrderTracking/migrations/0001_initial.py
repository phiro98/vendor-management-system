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
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_number', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('delivery_date', models.DateTimeField(null=True)),
                ('items', models.JSONField()),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('CANCELLED', 'Cancelled'), ('COMPLETED', 'Completed')], default='PENDING', max_length=20)),
                ('quality_rating', models.FloatField(blank=True, default=None, null=True)),
                ('delevery_on_time', models.BooleanField(default=False)),
                ('issue_date', models.DateTimeField(auto_now_add=True)),
                ('acknowledgment_date', models.DateTimeField(null=True)),
                ('vendor', models.ForeignKey(default=None, editable=False, on_delete=django.db.models.deletion.CASCADE, to='VendorProfileManagement.vendor')),
            ],
            options={
                'db_table': 'purchase_order',
            },
        ),
    ]
