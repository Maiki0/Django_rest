from rest_framework.routers import DefaultRouter
from apps.products.api.vi
from apps.products.api.viewsets.product_viewsets import ProductViewSets

router = DefaultRouter()

router.register(r'products', ProductViewSets, basename= 'products')
router.register(r'measure-unit', MeasureUnitViewSet, basename= 'measure_unit')
router.register(r'indicators', IndicatorViewSet, basename= 'Indicators')
router.register(r'category-products', CategoryProductsViewSet, basename= 'category_products')

urlpatterns = router.urls 

from apps.products.api.viewsets.general_views import *