from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import VendorProductMapping

class VendorProductMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorProductMapping
        fields = [
            'id', 'vendor', 'product', 'primary_mapping', 
            'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
        
        validators = [
            UniqueTogetherValidator(
                queryset=VendorProductMapping.objects.all(),
                fields=['vendor', 'product'],
                message="This vendor and product pair already exists."
            )
        ]

    def validate(self, data):
        """
        Object-level validation to ensure only one primary mapping per vendor[cite: 70, 75].
        """
        primary_mapping = data.get('primary_mapping')
        vendor = data.get('vendor')

        if primary_mapping:
            queryset = VendorProductMapping.objects.filter(vendor=vendor, primary_mapping=True)
            if self.instance:
                queryset = queryset.exclude(pk=self.instance.pk)
            if queryset.exists():
                raise serializers.ValidationError({
                    "primary_mapping": "This vendor already has a primary product mapping."
                })
        return data