from rest_framework.routers import DefaultRouter
from apps.products.api.views.product_viewsets import ProductViewSets

router = DefaultRouter()

router.register(r'products', ProductViewSets, basename= 'products')

urlpatterns = router.urls 