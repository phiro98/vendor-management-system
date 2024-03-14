from django.db import models
import uuid
from VendorProfileManagement.models import *
# Create your models here.
class HistoricalPerformance(models.Model):
   p_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key = True)
   vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
   date = models.DateTimeField(auto_now_add=True)
   on_time_delivery_rate = models.FloatField(null=True, blank=True, default=None)
   quality_rating_avg = models.FloatField(null=True, blank=True, default=None)
   average_response_time = models.FloatField(null=True, blank=True, default=None)
   fulfillment_rate = models.FloatField(null=True, blank=True, default=None)
   class Meta:
      db_table = "historical_performance"

   def __str__(self):
      return f"{self.p_id}"