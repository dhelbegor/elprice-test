from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from .models import Product
from .serializers import ProductSerializer
from .utils import makert_list_to_json




class BaseViewSerializer(object):
    serializer_class = ProductSerializer


class GetOrCreateProductView(BaseViewSerializer, ListCreateAPIView):
    def get_queryset(self):
            product = Product.objects.all()

            return product


class GetUpdateOrDeleteProductView(BaseViewSerializer, RetrieveUpdateDestroyAPIView):
    def get_queryset(self, pk):
        try:
            product = Product.objects.get(pk=pk)

        except product.DoesNotExist:
            content = {
                'status': 'Product Not Found.'
            }

            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return product

    def get(self, request, pk):
        product = self.get_queryset(pk)

        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        product = self.get_queryset(pk)
        serializer = ProductSerializer(product, request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_queryset(pk)
        product.delete()

        content = {
            'status': 'Product Does Not Exist.'
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)

def get_item(request):
    return JsonResponse(makert_list_to_json(), safe=False)
        
