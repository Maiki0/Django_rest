from django.urls import path

from apps.products.api.viewsets.general_views import MeasureUnitListAPIView, IndicatorListAPIView , CategoryProductsListAPIView



urlpatterns =[
    path('measure_unit/',MeasureUnitListAPIView.as_view(), name ='measure_unit'),
    path('indicator/',IndicatorListAPIView.as_view(), name ='indicator'),
 
  
    
]
    

