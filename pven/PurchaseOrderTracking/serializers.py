from rest_framework import serializers
from .models import *
from VendorProfileManagement.serializers import vendorSerializer

class POSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ['po_number','vendor', 'order_date', 'delivery_date', 'items','quantity','status','quality_rating','issue_date','acknowledgment_date','delevery_on_time']