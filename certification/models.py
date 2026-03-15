from core.models import BaseEntityModel

class Certification(BaseEntityModel):
    class Meta:
        verbose_name = "Certification"
        verbose_name_plural = "Certifications"
        db_table = "certifications"
        ordering = ['-created_at']