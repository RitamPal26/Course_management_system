from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.utils import APIViewMixin
from .models import Product
from .serializers import ProductSerializer
from drf_yasg.utils import swagger_auto_schema

class ProductListCreateAPIView(APIView, APIViewMixin):
    """
    List all products or create a new product.
    """
    @swagger_auto_schema(responses={200: ProductSerializer(many=True)})
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ProductSerializer, responses={201: ProductSerializer()})
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return self.error_response(serializer.errors)

class ProductDetailAPIView(APIView, APIViewMixin):
    """
    Retrieve, update or delete a product instance.
    """
    @swagger_auto_schema(responses={200: ProductSerializer()})
    def get(self, request, pk):
        product = self.get_object(Product, pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ProductSerializer, responses={200: ProductSerializer()})
    def put(self, request, pk):
        product = self.get_object(Product, pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return self.error_response(serializer.errors)

    @swagger_auto_schema(request_body=ProductSerializer, responses={200: ProductSerializer()})
    def patch(self, request, pk):
        product = self.get_object(Product, pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return self.error_response(serializer.errors)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        product = self.get_object(Product, pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)