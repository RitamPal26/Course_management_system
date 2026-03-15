from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from core.utils import APIViewMixin
from .models import VendorProductMapping
from .serializers import VendorProductMappingSerializer

class VendorProductMappingListCreateAPIView(APIView, APIViewMixin):
    """
    List or Create Vendor-Product Mappings with filtering support.
    """
    vendor_id_param = openapi.Parameter(
        'vendor_id', openapi.IN_QUERY, 
        description="Filter mappings by Vendor ID", 
        type=openapi.TYPE_INTEGER
    )

    @swagger_auto_schema(
        manual_parameters=[vendor_id_param],
        responses={200: VendorProductMappingSerializer(many=True)}
    )
    def get(self, request):
        """
        Handle GET requests with manual queryset filtering.
        """
        queryset = VendorProductMapping.objects.all()
        
        vendor_id = request.query_params.get('vendor_id')
        if vendor_id:
            queryset = queryset.filter(vendor_id=vendor_id)
            
        serializer = VendorProductMappingSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=VendorProductMappingSerializer, 
        responses={201: VendorProductMappingSerializer()}
    )
    def post(self, request):
        serializer = VendorProductMappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return self.error_response(serializer.errors)

class VendorProductMappingDetailAPIView(APIView, APIViewMixin):
    """
    Retrieve, Update, or Delete a specific mapping.
    """
    @swagger_auto_schema(responses={200: VendorProductMappingSerializer()})
    def get(self, request, pk):
        mapping = self.get_object(VendorProductMapping, pk)
        serializer = VendorProductMappingSerializer(mapping)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=VendorProductMappingSerializer, 
        responses={200: VendorProductMappingSerializer()}
    )
    def put(self, request, pk):
        mapping = self.get_object(VendorProductMapping, pk)
        serializer = VendorProductMappingSerializer(mapping, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return self.error_response(serializer.errors)

    @swagger_auto_schema(
        request_body=VendorProductMappingSerializer, 
        responses={200: VendorProductMappingSerializer()}
    )
    def patch(self, request, pk):
        mapping = self.get_object(VendorProductMapping, pk)
        serializer = VendorProductMappingSerializer(mapping, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return self.error_response(serializer.errors)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        mapping = self.get_object(VendorProductMapping, pk)
        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)