from rest_framework import serializers

from apps.expense_manager.models import Expense, Supplier

class SupplierRegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Supplier
        exclude = ('state','created_data','modified_data','deleted_data')

class ExpenseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Expense
        exclude = ('state','created_data','modified_data','deleted_data')