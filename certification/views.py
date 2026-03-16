from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.utils import APIViewMixin
from .models import Certification
from .serializers import CertificationSerializer
from drf_yasg.utils import swagger_auto_schema

class CertificationListCreateAPIView(APIView, APIViewMixin):
    """
    List all certifications or create a new certification [: 113-114].
    """
    @swagger_auto_schema(responses={200: CertificationSerializer(many=True)})
    def get(self, request):
        certifications = Certification.objects.all()
        serializer = CertificationSerializer(certifications, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CertificationSerializer, responses={201: CertificationSerializer()})
    def post(self, request):
        serializer = CertificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return self.error_response(serializer.errors)

class CertificationDetailAPIView(APIView, APIViewMixin):
    """
    Retrieve, update or delete a certification instance.
    """
    @swagger_auto_schema(responses={200: CertificationSerializer()})
    def get(self, request, pk):
        certification = self.get_object(Certification, pk)
        serializer = CertificationSerializer(certification)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CertificationSerializer, responses={200: CertificationSerializer()})
    def put(self, request, pk):
        certification = self.get_object(Certification, pk)
        serializer = CertificationSerializer(certification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return self.error_response(serializer.errors)

    @swagger_auto_schema(request_body=CertificationSerializer, responses={200: CertificationSerializer()})
    def patch(self, request, pk):
        certification = self.get_object(Certification, pk)
        serializer = CertificationSerializer(certification, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return self.error_response(serializer.errors)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        certification = self.get_object(Certification, pk)
        certification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)