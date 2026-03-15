from django.db import models
from django.core.exceptions import ValidationError
from core.models import BaseMappingModel
from vendor.models import Vendor
from product.models import Product

class VendorProductMapping(BaseMappingModel):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='product_mappings')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='vendor_mappings')

    class Meta:
        unique_together = ('vendor', 'product')

    def clean(self):
        """
        Custom validation: Only one primary mapping per Vendor.
        """
        if self.primary_mapping:
            queryset = VendorProductMapping.objects.filter(vendor=self.vendor, primary_mapping=True)
            if self.pk:
                queryset = queryset.exclude(pk=self.pk)
            if queryset.exists():
                raise ValidationError("This vendor already has a primary product mapping.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.vendor.name} -> {self.product.name}"