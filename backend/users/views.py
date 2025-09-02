from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def user_profile(request):
    """User profile endpoint placeholder"""
    return Response({
        'message': 'User profile endpoint - coming soon!'
    }, status=status.HTTP_200_OK)
