from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as rs
from VendorProfileManagement.models import *
from VendorPerformanceEvaluation.models import *
from VendorProfileManagement.serializers import vendorSerializer
from utilities.handler import *


# Create your views here.

class VendorView(APIView):
    def post(self, request):
        data = {}
        data['name'] = request.data.get('name')
        data['contact_details'] = request.data.get('contact_details')
        data['address'] = request.data.get('address')
        
        if not (data['name'] and data['contact_details'] and data['address']):
            return Response({"data":"Please enter valid details to create user"}, status=rs.HTTP_406_NOT_ACCEPTABLE)
        try:
            Vendor.objects.create(**data)
            return Response({"data":"vendor Created"}, status=rs.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"data":"Something Went Wrong"}, status=rs.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def get(self, request):
        vendor_code = self.request.query_params.get('id')
        try:
            queryset = Vendor.objects.all()
            resp = vendorSerializer(queryset, many = True).data              
            return Response({"data":resp}, status=rs.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"data":"Something Went Wrong"}, status=rs.HTTP_500_INTERNAL_SERVER_ERROR)
             
class DetailView(APIView):
    def get(self,request,vendor_code):
        if not is_valid_uuid(vendor_code):
            return Response({'data':"invalid vendor code"}, status= rs.HTTP_406_NOT_ACCEPTABLE)
        queryset = Vendor.objects.all() #filter(vendor_code=vendor_code).values()
        try:  
            resp = vendorSerializer(queryset.get(vendor_code=vendor_code)).data
            return Response({"data":resp}, status=rs.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"data":"Something Went Wrong"}, status=rs.HTTP_500_INTERNAL_SERVER_ERROR)
                
    def put(self, request, vendor_code):
        data = request.data        
        if not is_valid_uuid(vendor_code):
            return Response({'data':"invalid vendor code"}, status= rs.HTTP_406_NOT_ACCEPTABLE)
        try:
            vendor_details = Vendor.objects.get(vendor_code = vendor_code)
            resp = vendorSerializer(vendor_details, data=data, partial=True)
            if not resp.is_valid():
                return Response({'data':"invalid vendor data"}, status= rs.HTTP_406_NOT_ACCEPTABLE)
            resp.save()
            return Response({"data":"vendor updated"}, status=rs.HTTP_200_OK)
        except Exception as e:
            return Response({"data":"Something Went Wrong"}, status=rs.HTTP_500_INTERNAL_SERVER_ERROR)
    def delete(self, request, vendor_code):
        if not is_valid_uuid(vendor_code):
            return Response({'data':"invalid vendor code"}, status= rs.HTTP_406_NOT_ACCEPTABLE)
        try:
            v1 = Vendor.objects.filter(vendor_code=vendor_code).delete()
            return Response({"data":"vendor deleted"}, status=rs.HTTP_200_OK)
        except Exception as e:
            return Response({"data":"Something Went Wrong"}, status=rs.HTTP_500_INTERNAL_SERVER_ERROR)     
       
class VendorPerformance(APIView):
    def get(self,request,vendor_code):
        if not is_valid_uuid(vendor_code):
            return Response({'data':"invalid vendor code"}, status= rs.HTTP_406_NOT_ACCEPTABLE)
        try:
            queryset = HistoricalPerformance.objects.filter(vendor=vendor_code)
            resp = HistoricalPerformance.ob
        except Exception as e:
            return Response({"data":"Something Went Wrong"}, status=rs.HTTP_500_INTERNAL_SERVER_ERROR)     
                        