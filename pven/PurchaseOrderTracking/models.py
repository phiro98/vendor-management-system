from django.db import models
from VendorProfileManagement.models import *
import uuid
# Create your models here.
class PurchaseOrder(models.Model):
   po_number = models.UUIDField(default=uuid.uuid4, editable=False)
   vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
   order_date = models.DateTimeField(auto_now_add=True)
   delivery_date = models.DateTimeField(null =True) 
   items = models.JSONField(null=False)
   quantity = models.IntegerField()
   status_choices = [
        ('PENDING', 'Pending'),
        ('CANCELLED', 'Cancelled'),
        ('COMPLETED', 'Completed'),
    ]
   status = models.CharField(max_length=20, choices=status_choices, default='PENDING')
   quality_rating = models.FloatField(null=True, blank=True, default=None)
   delevery_on_time = models.BooleanField(default=False)
   issue_date = models.DateTimeField(auto_now_add=True) 
   acknowledgment_date = models.DateTimeField(null =True) ##
   
   class Meta:
      db_table = "purchase_order"

   def __str__(self):
      return f"{self.po_number}"