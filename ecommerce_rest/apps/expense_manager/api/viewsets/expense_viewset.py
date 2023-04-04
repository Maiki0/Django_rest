from django.db.models import Q

from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.expense_manager.models import Supplier
from apps.expense_manager.api.serializers.general_serializer import SupplierSerializer
from apps.expense_manager.api.serializers.expense_serializer import *


class ExpenseViwSet(viewsets.GenericViewSet):
    serializer_class = ExpenseSerializer
    
    @action(methods=['get'], detail= False)
    def search_supplier(self, request):
        ruc_or_business_name = request.query_params.get('ruc_or_business_name', '')
        supplier = Supplier.objects.filter(
            Q(ruc__iexact = ruc_or_business_name) |
            Q(business_name__iexact = ruc_or_business_name )
        ).filter()
        if supplier:
            supplier_serilaizer = SupplierSerializer(supplier)
            return Response(supplier_serilaizer.data,status=status.HTTP_200_OK)
        return Response({'mensaje':'No se a encotrado un Proveedor'},status=status.HTTP_404_NOT_FOUND)
    
    
    @action(methods=['post'], detail= False)
    def new_supplier(self, request):
        pass