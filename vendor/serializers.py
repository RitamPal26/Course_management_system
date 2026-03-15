# vendor/serializers.py
from rest_framework import serializers
from .models import Vendor

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = [
            'id', 'name', 'code', 'description', 
            'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_name(self, value):
        """
        Example of field-level validation: Ensure name isn't just whitespace.
        """
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty or just whitespace.")
        return value