from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser

from apps.base.utils import validate_files
from apps.products.api.serializers.product_serializers import CategoryProductSerializer

class CategoryProductViewset(viewsets.ModelViewSet):
    serializer_class = CategoryProductSerializer
    parser_classes = (JSONParser, MultiPartParser,)
    
    
    def get_queryset(self, pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk, state = True ).first()
    
    def list(self, request):
        category_product = self.get_serializer(self.get_queryset(),many = True)
        return Response(category_product.data, status = status.HTTP_200_OK)
    
    
    def create(self,request):
        # send information to seralizer
        data = request.data
        serializer = self.serializer_class(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Producto creado correctamente!'},status=status.HTTP_201_CREATED)
        return Response ({'message':'', 'erro' : serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    
    
    
    def update(self, request, pk = None):
        
        data = request.data
        if self.get_queryset(pk):
            
            category_product_serializer = self.serializer_class(self.get_queryset(pk),data = data)
            if category_product_serializer.is_valid():
                category_product_serializer.save()
                return Response(category_product_serializer.data,status=status.HTTP_200_OK)
            return Response(category_product_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self,request,pk=None):
        category_product = self.get_queryset().filter(id = pk).first()
        if category_product:
            category_product.state = False
            category_product.save()
            return Response({'message':'Producto eliminado correctamente!'},status=status.HTTP_200_OK)
        return Response({'error':'No existe ningun produdcto con estos datos!'}, status=status.HTTP_400_BAD_REQUEST) 
         
            
 