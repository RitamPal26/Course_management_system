# vendor/models.py
from core.models import BaseEntityModel

class Vendor(BaseEntityModel):
    """
    Vendor master entity.
    Inherits common fields and unique 'code' validation from BaseEntityModel.
    """
    class Meta:
        verbose_name = "Vendor"
        verbose_name_plural = "Vendors"
        db_table = "vendors"
        ordering = ['-created_at']