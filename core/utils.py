# core/utils.py
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

class APIViewMixin:
    """
    Utility mixin to provide common functionality for APIViews.
    Follows DRY principles for object fetching and error handling.
    """
    
    def get_object(self, model, pk):
        """
        Safely fetch an object by PK or raise a 404.
        Satisfies the 'handling Does Not Exist' requirement.
        """
        try:
            return model.objects.get(pk=pk)
        except model.DoesNotExist:
            raise Http404

    def error_response(self, errors, message="Validation Failed", status_code=status.HTTP_400_BAD_REQUEST):
        """
        Standardized error response format.
        """
        return Response({
            "message": message,
            "errors": errors
        }, status=status_code)