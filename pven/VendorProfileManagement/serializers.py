from rest_framework import serializers
from .models import *


class vendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['vendor_code', 'name', 'contact_details', 'address','on_time_delivery_rate','quality_rating_avg','average_response_time','fulfillment_rate']