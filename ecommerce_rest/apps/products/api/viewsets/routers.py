from rest_framework.routers import DefaultRouter
from apps.products.api.viewsets.general_views import *
from apps.products.api.viewsets.product_viewsets import ProductViewSets
from apps. products.api.viewsets.category_product_viewswts import CategoryProductViewset
from apps.products.api.viewsets.mesure_unitviewset import MeasureUnitViewSet
from apps.products.api.viewsets.indicatorviewset import IndicatorViewSet

router = DefaultRouter()

router.register(r'products', ProductViewSets, basename= 'products')
router.register(r'measure-unit', MeasureUnitViewSet, basename= 'measure_unit')
router.register(r'indicators', IndicatorViewSet, basename= 'Indicators')
router.register(r'category-products', CategoryProductViewset, basename= 'category_products')

urlpatterns = router.urls 

