from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def help_requests_list(request):
    """Help requests list endpoint placeholder"""
    return Response({
        'message': 'Help requests endpoint - coming soon!',
        'data': []
    }, status=status.HTTP_200_OK)
