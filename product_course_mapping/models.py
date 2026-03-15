from django.db import models
from django.core.exceptions import ValidationError
from core.models import BaseMappingModel
from product.models import Product
from course.models import Course

class ProductCourseMapping(BaseMappingModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='course_mappings')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='product_mappings')

    class Meta:
        unique_together = ('product', 'course')

    def clean(self):
        if self.primary_mapping:
            queryset = ProductCourseMapping.objects.filter(product=self.product, primary_mapping=True)
            if self.pk:
                queryset = queryset.exclude(pk=self.pk)
            if queryset.exists():
                raise ValidationError("This product already has a primary course mapping.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)