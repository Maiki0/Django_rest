from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel
# Create your models here.

class MeasureUnit(BaseModel):

    description = models.CharField('Descripcion', max_length= 50, blank=False, null= False, unique= True)
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by    
    
    @_history_user.setter
    def _history_user(self, value):
        return self.changed_by 
    
    
    class Meta:
        verbose_name = 'Unidad de medida'
        verbose_name_plural = 'Unidades de medidas'
        
    def __str__(self):
        return self.description
    
    
class CategoryProduct(BaseModel):
    
    description = models.CharField('Descripcion', max_length= 50, unique= True, null= False, blank= False)

    historical = HistoricalRecords()
        
    @property
    def _history_user(self):
        return self.changed_by    
    
    @_history_user.setter
    def _history_user(self, value):
        return self.changed_by 
    
    
    
    class Meta:        
        verbose_name =  'Categoria de producto ' 
        verbose_name_plural =  'Categorias de productos'
            
     
    def __str__(self):
        return self.description 
    
    
    
    
class Indicator(BaseModel):
    
    descount_value = models.PositiveSmallIntegerField(default= 0)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name= 'Indicador de oferta')
    historicla = HistoricalRecords() 
    
    
    @property
    def _history_user(self):
        return self.changed_by    
    
    @_history_user.setter
    def _history_user(self, value):
        return self.changed_by
      
    
    class Meta:
        verbose_name = 'Indicador de Oferta'
        verbose_name_plural = 'Indicadores de Ofertas'
        
    def __str__(self):
        return f'Oferta de categoria {self.category_product}: { self.descount_value}%'
    
    
class Product(BaseModel):

    name = models.CharField('Nombre del producto', max_length=150, unique= True, null=False, blank=False)
    description = models.TextField('Descripcion del producto', null=False , blank=False)
    image = models.ImageField('Imagen del Producto', upload_to='products/', blank=True ,null=True)
    measure_unit= models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de medida', null= True)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='categorya de producto', null=True)        
    historical = HistoricalRecords()
    
    
    
    @property
    def _history_user(self):
        return self.changed_by    
    
    @_history_user.setter
    def _history_user(self, value):
        return self.changed_by
      
    
    
    class Meta:
      verbose_name = 'Produtos'
      verbose_name_plural ='Productos'        
        
    
    def __str__(self):
        return self.name
