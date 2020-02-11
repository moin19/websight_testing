from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from news.models import *
from .serializers import *

class products_detail_all(generics.ListAPIView):
    serializer_class = ProductsSalesSerializer
    def get_queryset(self):
        app_user_id = self.request.session.get('app_user_id')
        queryset = Products_Sales.objects.filter().order_by('-app_data_time')

        return queryset


@api_view(['GET', 'PUT', 'DELETE'])
def products_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        products = Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductsSalesSerializer(products)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductsSalesSerializer(products, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)