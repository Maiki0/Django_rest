from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser

from apps.products.api.serializers.general_serializers import IndicatorSerializer

class IndicatorViewSet(viewsets.ModelViewSet):
    serializer_class = IndicatorSerializer
    parser_classes = (JSONParser, MultiPartParser,)
    
    
    def get_queryset(self, pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk, state = True ).first()
    
    def list(self, request):
        indicator = self.get_serializer(self.get_queryset(),many = True)
        return Response(indicator.data, status = status.HTTP_200_OK)
    
    
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
            
            indicator = self.serializer_class(self.get_queryset(pk),data = data)
            if indicator.is_valid():
                indicator.save()
                return Response(indicator.data,status=status.HTTP_200_OK)
            return Response(indicator.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self,request,pk=None):
        indicator = self.get_queryset().filter(id = pk).first()
        if indicator:
            indicator.state = False
            indicator.save()
            return Response({'message':'Producto eliminado correctamente!'},status=status.HTTP_200_OK)
        return Response({'error':'No existe ningun produdcto con estos datos!'}, status=status.HTTP_400_BAD_REQUEST) 
         
            
 