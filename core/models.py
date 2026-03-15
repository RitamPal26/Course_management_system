# core/models.py
import uuid
from django.db import models

class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    'created_at' and 'updated_at' fields.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class BaseEntityModel(TimeStampedModel):
    """
    Abstract base for Master Entities: Vendor, Product, etc.
    """
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name} ({self.code})"
    
class BaseMappingModel(TimeStampedModel):
    """
    Abstract base for all Mapping entities.
    Handles primary status, active flag, and timestamps.
    """
    primary_mapping = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True