from rest_framework import viewsets
from rest_framework.response import Response

from apps.base.api import GeneralListAPIView
from apps.products.models import MeasureUnit
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, IndicatorSerializer, CategoryProductSerializer


class MeasureUnitViewSet(viewsets.GenericViewSet):
    ''' 
    Hola desde unidad de medida 
    '''
    
    model = MeasureUnit
    serializer_class = MeasureUnitSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)
    
    def list (self,request):
        '''
        Retorna toda las unidades de medida disponible
        
        
        params.
        name ----> nombre de la unidad de media disponible 
        '''
        
        data = self.get_queryset()
        data = self.get_serializer(data,many= True)
        return Response (data.data)
    
    
    def create (self, request):
        return Response({})
        
    
class IndicatorViewSet(viewsets.GenericViewSet):
    serializer_class = IndicatorSerializer
    
    
    model = MeasureUnit
    serializer_class = MeasureUnitSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)
    
    def list (self,request):
       
        
        data = self.get_queryset()
        data = self.get_serializer(data,many= True)
        return Response (data.data)
    
    
    def create (self, request):
        return Response({})
    
       

'''class CategoryProductsViewSet(viewsets.GenericViewSet):
    serializer_class = CategoryProductSerializer
    
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)
    
    def list (self,request):
       
        
        data = self.get_queryset()
        data = self.get_serializer(data,many= True)
        return Response (data.data)
    
    
    def create (self, request):
        return Response({})'''