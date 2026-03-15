from django.db import models
from django.core.exceptions import ValidationError
from core.models import BaseMappingModel
from course.models import Course
from certification.models import Certification

class CourseCertificationMapping(BaseMappingModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='certification_mappings')
    certification = models.ForeignKey(Certification, on_delete=models.CASCADE, related_name='course_mappings')

    class Meta:
        unique_together = ('course', 'certification')

    def clean(self):
        if self.primary_mapping:
            queryset = CourseCertificationMapping.objects.filter(course=self.course, primary_mapping=True)
            if self.pk:
                queryset = queryset.exclude(pk=self.pk)
            if queryset.exists():
                raise ValidationError("This course already has a primary certification mapping.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)