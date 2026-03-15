from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import ProductCourseMapping

class ProductCourseMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCourseMapping
        fields = [
            'id', 'product', 'course', 'primary_mapping', 
            'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

        validators = [
            UniqueTogetherValidator(
                queryset=ProductCourseMapping.objects.all(),
                fields=['product', 'course'],
                message="This product and course pair already exists." [cite: 73]
            )
        ]

    def validate(self, data):
        if data.get('primary_mapping'):
            product = data.get('product')
            queryset = ProductCourseMapping.objects.filter(product=product, primary_mapping=True)
            if self.instance:
                queryset = queryset.exclude(pk=self.instance.pk)
            if queryset.exists():
                raise serializers.ValidationError({
                    "primary_mapping": "This product already has a primary course mapping."
                })
        return data