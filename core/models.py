# core/models.py
import uuid
from django.db import models

class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    'created_at' and 'updated_at' fields.
    """
    created_at = models.DateTimeField(auto_now_add=True) [cite: 50, 58]
    updated_at = models.DateTimeField(auto_now=True) [cite: 51, 59]

    class Meta:
        abstract = True

class BaseEntityModel(TimeStampedModel):
    """
    Abstract base for Master Entities: Vendor, Product, etc.
    """
    name = models.CharField(max_length=255) [cite: 46]
    code = models.CharField(max_length=100, unique=True) [cite: 47, 67]
    description = models.TextField(blank=True, null=True) [cite: 48]
    is_active = models.BooleanField(default=True) [cite: 49]

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name} ({self.code})"