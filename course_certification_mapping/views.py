from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from core.utils import APIViewMixin
from .models import CourseCertificationMapping
from .serializers import CourseCertificationMappingSerializer

class CourseCertificationMappingListCreateAPIView(APIView, APIViewMixin):
    """
    List or Create Course-Certification Mappings.
    Supports filtering by course_id.
    """
    course_id_param = openapi.Parameter(
        'course_id', openapi.IN_QUERY, 
        description="Filter mappings by Course ID", 
        type=openapi.TYPE_INTEGER
    )

    @swagger_auto_schema(
        manual_parameters=[course_id_param],
        responses={200: CourseCertificationMappingSerializer(many=True)}
    )
    def get(self, request):
        queryset = CourseCertificationMapping.objects.all()
        course_id = request.query_params.get('course_id')
        
        if course_id:
            queryset = queryset.filter(course_id=course_id)
            
        serializer = CourseCertificationMappingSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=CourseCertificationMappingSerializer, 
        responses={201: CourseCertificationMappingSerializer()}
    )
    def post(self, request):
        serializer = CourseCertificationMappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return self.error_response(serializer.errors)

class CourseCertificationMappingDetailAPIView(APIView, APIViewMixin):
    """
    Retrieve, Update, or Delete a specific course-certification mapping.
    """
    @swagger_auto_schema(responses={200: CourseCertificationMappingSerializer()})
    def get(self, request, pk):
        mapping = self.get_object(CourseCertificationMapping, pk)
        serializer = CourseCertificationMappingSerializer(mapping)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=CourseCertificationMappingSerializer, 
        responses={200: CourseCertificationMappingSerializer()}
    )
    def put(self, request, pk):
        mapping = self.get_object(CourseCertificationMapping, pk)
        serializer = CourseCertificationMappingSerializer(mapping, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return self.error_response(serializer.errors)

    @swagger_auto_schema(
        request_body=CourseCertificationMappingSerializer, 
        responses={200: CourseCertificationMappingSerializer()}
    )
    def patch(self, request, pk):
        mapping = self.get_object(CourseCertificationMapping, pk)
        serializer = CourseCertificationMappingSerializer(mapping, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return self.error_response(serializer.errors)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        mapping = self.get_object(CourseCertificationMapping, pk)
        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)