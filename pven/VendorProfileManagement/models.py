from django.db import models
import uuid
# Create your models here.
class Vendor(models.Model):
   vendor_code = models.UUIDField(default=uuid.uuid4, editable=False, primary_key = True)
   name = models.CharField(max_length=40)
   contact_details = models.CharField(max_length=20,unique=True)
   address = models.CharField(max_length=3000)
   on_time_delivery_rate = models.FloatField(null=True, blank=True, default=None)
   quality_rating_avg = models.FloatField(null=True, blank=True, default=None)
   average_response_time = models.FloatField(null=True, blank=True, default=None)
   fulfillment_rate = models.FloatField(null=True, blank=True, default=None)
   class Meta:
      db_table = "vendor"

   def __str__(self):
      return f"{self.vendor_code}"
