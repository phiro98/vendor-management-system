from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as rs
from PurchaseOrderTracking.models import *
from PurchaseOrderTracking.serializers import POSerializer
from VendorProfileManagement.serializers import vendorSerializer
from utilities.handler import *
import json
from datetime import datetime
from django.utils import timezone





# Create your views here.

class POView(APIView):
    def post(self, request):
        data = {}
        data['vendor'] = Vendor.objects.get(vendor_code=request.data.get('vendor')).pk
        data['delivery_date'] = datetime.strptime(request.data.get('delivery_date'), '%d/%m/%Y %H:%M:%S')
        data['address'] = request.data.get('address')
        data['items'] = json.loads(request.data.get('items').replace("'",'"')) #json.loads()
        data['quantity'] = request.data.get('quantity')

        if not (data['vendor'] and data['address'] and data['items'] and data['quantity']):
            return Response({"data":"Please enter valid details to create Purchase order"}, status=rs.HTTP_406_NOT_ACCEPTABLE)
        try:
            resp = POSerializer(data=data)
            if resp.is_valid(raise_exception=True):
                resp.save()
            return Response({"data":"Purchase order Created"}, status=rs.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"data":"Something Went Wrong"}, status=rs.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def get(self, request):
        try:
            queryset = PurchaseOrder.objects.all()
            resp = POSerializer(queryset, many = True).data              
            return Response({"data":resp}, status=rs.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"data":"Something Went Wrong"}, status=rs.HTTP_500_INTERNAL_SERVER_ERROR)
             
class PODetailView(APIView):
    def get(self,request,po_number):
        if not is_valid_uuid(po_number):
            return Response({'data':"invalid po_number"}, status= rs.HTTP_406_NOT_ACCEPTABLE)
        queryset = PurchaseOrder.objects.all() #filter(vendor_code=vendor_code).values()
        try:  
            resp = POSerializer(queryset.get(po_number=po_number)).data
            print(resp) 
            return Response({"data":resp}, status=rs.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"data":"Something Went Wrong"}, status=rs.HTTP_500_INTERNAL_SERVER_ERROR)
                
    def put(self, request, po_number):
        data = request.data        
        if not is_valid_uuid(po_number):
            return Response({'data':"invalid po_number"}, status= rs.HTTP_406_NOT_ACCEPTABLE)
        try:
            PO_details = PurchaseOrder.objects.get(po_number = po_number)
            if data.get('status').lower()=='completed' and PO_details.delivery_date > timezone.now():
                data["delevery_on_time"]=True
            resp = POSerializer(PO_details, data=data, partial=True)
            if not resp.is_valid():
                return Response({'data':"invalid Purchase Order"}, status= rs.HTTP_406_NOT_ACCEPTABLE)
            resp.save()
            #setting performance
            if data.get("delevery_on_time", False): set_on_time_delivery_rate(resp.data["vendor"])
            if data.get("quality_rating", False): set_quality_rating_avg(resp.data["vendor"])
            if data.get("status", False): set_fulfillment_rate(resp.data["vendor"])   
                             
            return Response({"data":"Purchase Order updated"}, status=rs.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"data":"Something Went Wrong"}, status=rs.HTTP_500_INTERNAL_SERVER_ERROR)
    def delete(self, request, po_number):
        if not is_valid_uuid(po_number):
            return Response({'data':"invalid po_number"}, status= rs.HTTP_406_NOT_ACCEPTABLE)
        try:
            PurchaseOrder.objects.filter(po_number=po_number).delete()
            return Response({"data":"Purchase Order deleted"}, status=rs.HTTP_200_OK)
        except Exception as e:
            return Response({"data":"Something Went Wrong"}, status=rs.HTTP_500_INTERNAL_SERVER_ERROR)     
       
class POacknowledge(APIView):
    def post(self, request, po_number):
        if not is_valid_uuid(po_number) and not bool(request.data.get('acknowledge')):
            return Response({'data':"invalid data"}, status= rs.HTTP_406_NOT_ACCEPTABLE)
        try:
            PO_details = PurchaseOrder.objects.get(po_number = po_number)
            data = {"acknowledgment_date":datetime.now()}
            resp = POSerializer(PO_details, data=data, partial=True)
            if not resp.is_valid():
                return Response({'data':"invalid Purchase Order"}, status= rs.HTTP_406_NOT_ACCEPTABLE)
            resp.save()
            set_average_response_time(resp.data["vendor"])
            return Response({"data":"Purchase Order updated"}, status=rs.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"data":"Something Went Wrong"}, status=rs.HTTP_500_INTERNAL_SERVER_ERROR)
            
                     