from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.
class BaseModel(models.Model):
    '''Model definition for BaseModel'''
    id = models.AutoField(primary_key=True)
    state = models.BooleanField('Estado', default=True)
    created_data = models.DateField('Fecha de creacion',auto_now= False, auto_now_add= True)
    modified_data = models.DateField('Fecha de modificacion', auto_now= True, auto_now_add=False)
    deleted_data = models.DateField('Fecha de eliminacion', auto_now= False, auto_now_add=True)
    historical = HistoricalRecords( user_model= "users.User", inherit=True)
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self,value):
        return self.changed_by
    
    
    class Meta:
        '''Meta definition for BaseModel'''
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'