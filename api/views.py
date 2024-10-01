from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProductSerializer
from Product.models import Product

# Create your views here.
class ProductListView(APIView):
    def get(self,request):
        products =Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
def post(self,request):
    serializer= ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
class ProductDetailView(APIView):
    def get(self, request, id, format=None):
        product= self.get_object(id) 
        serializer=ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self,request, id ,format=None):
        product=self.get_object(id)
        serializer=ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id, format=None):
        product= self.get_object(id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  
    
