from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.utils import APIViewMixin
from .models import Vendor
from .serializers import VendorSerializer
from drf_yasg.utils import swagger_auto_schema

class VendorListCreateAPIView(APIView, APIViewMixin):
    """
    List all vendors or create a new vendor.
    """
    @swagger_auto_schema(responses={200: VendorSerializer(many=True)})
    def get(self, request):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=VendorSerializer, responses={201: VendorSerializer()})
    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return self.error_response(serializer.errors)

class VendorDetailAPIView(APIView, APIViewMixin):
    """
    Retrieve, update or delete a vendor instance.
    """
    @swagger_auto_schema(responses={200: VendorSerializer()})
    def get(self, request, pk):
        vendor = self.get_object(Vendor, pk)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=VendorSerializer, responses={200: VendorSerializer()})
    def put(self, request, pk):
        vendor = self.get_object(Vendor, pk)
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return self.error_response(serializer.errors)

    @swagger_auto_schema(request_body=VendorSerializer, responses={200: VendorSerializer()})
    def patch(self, request, pk):
        vendor = self.get_object(Vendor, pk)
        serializer = VendorSerializer(vendor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return self.error_response(serializer.errors)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        vendor = self.get_object(Vendor, pk)
        vendor.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)