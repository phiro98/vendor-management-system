from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from utilities.handler import *
from rest_framework import status as rs
from VendorPerformanceEvaluation.serializers import *



# Create your views here.
class performanceView(APIView):
    def get(self, request, vendor_code):
        if not is_valid_uuid(vendor_code):
            return Response({'data':"invalid vendor code"}, status= rs.HTTP_406_NOT_ACCEPTABLE)
        data = {}
        try:  
            queryset = Vendor.objects.all() #filter(vendor_code=vendor_code).values()
            resp = vendorSerializer(queryset.get(vendor_code=vendor_code)).data
            data["on_time_delivery_rate"] = resp["on_time_delivery_rate"]
            data["quality_rating_avg"] = resp["quality_rating_avg"]
            data["average_response_time"] = resp["average_response_time"]
            data["fulfillment_rate"] = resp["fulfillment_rate"]
            data["vendor"] = vendor_code
            resp = performanceSerializer(data=data)
            if resp.is_valid(raise_exception=True):
                resp.save()
            resp = performanceSerializer(HistoricalPerformance.objects.all(), many = True).data
            return Response({"data":resp}, status=rs.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"data":"Something Went Wrong"}, status=rs.HTTP_500_INTERNAL_SERVER_ERROR)
