from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser

from apps.base.utils import validate_files
from apps.products.api.serializers.product_serializers import ProductSerializer

class ProductViewSets(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    parser_classes = (JSONParser, MultiPartParser,)
    
    
    def get_queryset(self, pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk, state = True ).first()
    
    def list(self, request):
        product_serializer = self.get_serializer(self.get_queryset(),many = True)
        return Response(product_serializer.data, status = status.HTTP_200_OK)
    
    
    def create(self,request):
        # send information to seralizer
        data = validate_files(request.data, 'image')
        serializer = self.serializer_class(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Producto creado correctamente!'},status=status.HTTP_201_CREATED)
        return Response ({'message':'', 'erro' : serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    
    
    
    def update(self, request, pk = None):
        if self.get_queryset(pk):
            
            data = validate_files(request.data,'image', True)
            product_serializer = self.serializer_class(self.get_queryset(pk),data =data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data,status=status.HTTP_200_OK)
            return Response(product_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self,request,pk=None):
        product = self.get_queryset().filter(id = pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message':'Producto eliminado correctamente!'},status=status.HTTP_200_OK)
        return Response({'error':'No existe ningun produdcto con estos datos!'}, status=status.HTTP_400_BAD_REQUEST) 
         
            
 