import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class ShippingFeeZone(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    shipping_fee = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name 
    

class Country(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=4)
    tel = models.CharField(max_length=4)
    # has_states = models.BooleanField(default=False)
    # shipping_fee = models.ForeignKey(ShippingFeeZone,on_delete=models.PROTECT,related_name="countries", null=True, blank=True)
    shipping_zones = models.ManyToManyField(ShippingFeeZone, related_name="countries", blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
            verbose_name_plural = "Countries"


    def __str__(self):
        return self.name
    
    
    
  
    