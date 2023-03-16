from rest_framework import serializers

from apps.products.models import Product
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer


class ProductSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Product
        exclude =('state','created_data','modified_data','deleted_data')

    def validate_measure_unit(self, value):
        if value == '' or value == None:
            raise serializers.ValidationError('Debes ingresar la Unidad de Medida')
        return value
    
    def validate_category_product(self, value):
        if value == '' or value == None:
            raise serializers.ValidationError('Debes ingresar la Categoria de Productos ')
        
    def validate(self, data):
        if 'mesure_unit' not in data.keys():
            raise serializers.ValidationError({'measeur_uni':'Debes ingresar Unida de Medida'})
        
        if 'category_product' not in data.keys():
            raise serializers.ValidationError({'category_product ':'Debes ingresar Categoria de Productos'})
        return data 
    
        
    def to_representation(self, instance):
        return {
            'id':instance.id,
            'name':instance.name,
            'description':instance.description,
            'image':instance.image.url if instance.image != '' else '',
            'measure_unit':instance.measure_unit.description if instance.measure_unit is not None else '',
            'category_product':instance.category_product.description if instance.category_product is not None else''
        }