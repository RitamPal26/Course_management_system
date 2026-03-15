from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import CourseCertificationMapping

class CourseCertificationMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCertificationMapping
        fields = [
            'id', 'course', 'certification', 'primary_mapping', 
            'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

        validators = [
            UniqueTogetherValidator(
                queryset=CourseCertificationMapping.objects.all(),
                fields=['course', 'certification'],
                message="This course and certification pair already exists." [cite: 74]
            )
        ]

    def validate(self, data):
        if data.get('primary_mapping'):
            course = data.get('course')
            queryset = CourseCertificationMapping.objects.filter(course=course, primary_mapping=True)
            if self.instance:
                queryset = queryset.exclude(pk=self.instance.pk)
            if queryset.exists():
                raise serializers.ValidationError({
                    "primary_mapping": "This course already has a primary certification mapping."
                })
        return data