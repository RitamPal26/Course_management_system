from core.models import BaseEntityModel

class Course(BaseEntityModel):
    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        db_table = "courses"
        ordering = ['-created_at']