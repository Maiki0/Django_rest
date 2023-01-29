from rest_framework.routers import DefaultRouter
from apps.products.api.views.general_views import *
from apps.products.api.views.product_viewsets import ProductViewSets

router = DefaultRouter()

router.register(r'products', ProductViewSets, basename= 'products')
router.register(r'measure-unit', MeasureUnitViewSet, basename= 'measure_unit')
router.register(r'indicators', IndicatorViewSet, basename= 'Indicators')
router.register(r'category-products', CategoryProductsViewSet, basename= 'category_products')

urlpatterns = router.urls 