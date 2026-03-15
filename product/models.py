from core.models import BaseEntityModel

class Product(BaseEntityModel):
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        db_table = "products"
        ordering = ['-created_at']