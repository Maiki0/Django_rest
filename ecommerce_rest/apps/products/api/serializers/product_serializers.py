from rest_framework import serializers

from apps.products.models import Product
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer


class ProductSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Product
        exclude =('state','created_data','modified_data','deleted_data')
        
        
    def to_representation(self, instance):
        return {
            'id':instance.id,
            'name':instance.name,
            'description':instance.description,
            'image':instance.image if instance.image != '' else '',
            'measure_unit':instance.measure_unit.description if instance.measure_unit is not None else '',
            'category_product':instance.category_product.description if instance.category_product is not None else''
        }