import uuid
from PurchaseOrderTracking.models import PurchaseOrder
from VendorProfileManagement.models import Vendor
from VendorProfileManagement.serializers import vendorSerializer
from VendorPerformanceEvaluation.models import HistoricalPerformance
from PurchaseOrderTracking.serializers import POSerializer
from datetime import datetime

def set_on_time_delivery_rate(vendor):
    ontime_po_completed = PurchaseOrder.objects.filter(vendor = vendor, delevery_on_time = True).count() 
    total_po_completed = PurchaseOrder.objects.filter(vendor = vendor, status = "COMPLETED").count()
    if total_po_completed>0:
        data = {"on_time_delivery_rate":ontime_po_completed*100/total_po_completed}
        vendor_details = Vendor.objects.get(vendor_code = vendor)
        resp = vendorSerializer(vendor_details, data=data, partial=True)
        if resp.is_valid(raise_exception=True):
            resp.save()

def set_quality_rating_avg(vendor):
    ratings = PurchaseOrder.objects.filter(vendor = vendor, status = "COMPLETED").values_list("quality_rating")
    rating_list = [x[0] for x in list(ratings)]
    if rating_list: 
        data = {"quality_rating_avg": sum(rating_list)/len(rating_list)}
        vendor_details = Vendor.objects.get(vendor_code = vendor)
        resp = vendorSerializer(vendor_details, data=data, partial=True)
        if resp.is_valid(raise_exception=True):
                resp.save()
def set_average_response_time(vendor):
    ratings = list(PurchaseOrder.objects.filter(vendor = vendor, acknowledgment_date__isnull=False).values_list("issue_date","acknowledgment_date"))
    difference = [(x[1]-x[0]).seconds for x in ratings]
    data = {"average_response_time": sum(difference)/len(difference)}
    vendor_details = Vendor.objects.get(vendor_code = vendor)
    resp = vendorSerializer(vendor_details, data=data, partial=True)
    if resp.is_valid(raise_exception=True):
            resp.save()
def set_fulfillment_rate(vendor):
    successful_po = PurchaseOrder.objects.filter(vendor = vendor, delevery_on_time = True).count() 
    total_po = PurchaseOrder.objects.filter(vendor = vendor).count()   
    if total_po>0:
        data = {"fulfillment_rate":successful_po*100/total_po}
        vendor_details = Vendor.objects.get(vendor_code = vendor)
        resp = vendorSerializer(vendor_details, data=data, partial=True)
        if resp.is_valid(raise_exception=True):
            resp.save()         
def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False