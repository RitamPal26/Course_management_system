from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from core.utils import APIViewMixin
from .models import ProductCourseMapping
from .serializers import ProductCourseMappingSerializer

class ProductCourseMappingListCreateAPIView(APIView, APIViewMixin):
    """
    List or Create Product-Course Mappings.
    Supports filtering by product_id[cite: 160].
    """
    product_id_param = openapi.Parameter(
        'product_id', openapi.IN_QUERY, 
        description="Filter mappings by Product ID", 
        type=openapi.TYPE_INTEGER
    )

    @swagger_auto_schema(
        manual_parameters=[product_id_param],
        responses={200: ProductCourseMappingSerializer(many=True)}
    )
    def get(self, request):
        queryset = ProductCourseMapping.objects.all()
        product_id = request.query_params.get('product_id')
        
        if product_id:
            queryset = queryset.filter(product_id=product_id)
            
        serializer = ProductCourseMappingSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=ProductCourseMappingSerializer, 
        responses={201: ProductCourseMappingSerializer()}
    )
    def post(self, request):
        serializer = ProductCourseMappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return self.error_response(serializer.errors)

class ProductCourseMappingDetailAPIView(APIView, APIViewMixin):
    """
    Retrieve, Update, or Delete a specific product-course mapping.
    """
    @swagger_auto_schema(responses={200: ProductCourseMappingSerializer()})
    def get(self, request, pk):
        mapping = self.get_object(ProductCourseMapping, pk)
        serializer = ProductCourseMappingSerializer(mapping)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=ProductCourseMappingSerializer, 
        responses={200: ProductCourseMappingSerializer()}
    )
    def put(self, request, pk):
        mapping = self.get_object(ProductCourseMapping, pk)
        serializer = ProductCourseMappingSerializer(mapping, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return self.error_response(serializer.errors)

    @swagger_auto_schema(
        request_body=ProductCourseMappingSerializer, 
        responses={200: ProductCourseMappingSerializer()}
    )
    def patch(self, request, pk):
        mapping = self.get_object(ProductCourseMapping, pk)
        serializer = ProductCourseMappingSerializer(mapping, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return self.error_response(serializer.errors)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        mapping = self.get_object(ProductCourseMapping, pk)
        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)