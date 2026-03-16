from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.utils import APIViewMixin
from .models import Course
from .serializers import CourseSerializer
from drf_yasg.utils import swagger_auto_schema

class CourseListCreateAPIView(APIView, APIViewMixin):
    """
    List all courses or create a new course.
    """
    @swagger_auto_schema(responses={200: CourseSerializer(many=True)})
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CourseSerializer, responses={201: CourseSerializer()})
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return self.error_response(serializer.errors)

class CourseDetailAPIView(APIView, APIViewMixin):
    """
    Retrieve, update or delete a course instance.
    """
    @swagger_auto_schema(responses={200: CourseSerializer()})
    def get(self, request, pk):
        course = self.get_object(Course, pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CourseSerializer, responses={200: CourseSerializer()})
    def put(self, request, pk):
        course = self.get_object(Course, pk)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return self.error_response(serializer.errors)

    @swagger_auto_schema(request_body=CourseSerializer, responses={200: CourseSerializer()})
    def patch(self, request, pk):
        course = self.get_object(Course, pk)
        serializer = CourseSerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return self.error_response(serializer.errors)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        course = self.get_object(Course, pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)