from django.contrib import admin
from django.urls import path,include,re_path
from django.views.static import serve
from django.conf import settings
from rest_framework import permissions 
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from apps.users.views import Login,Logout

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="Documentacion de API",
      default_version='v0.1',
      description="Documentacion publica de Api de Ecommerce",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="oscarbrazoban@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',Login.as_view(), name='login'),
    path('Logout/',Logout.as_view(), name='Logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('usuario/',include('apps.users.api.routers')),
    path('products/',include('apps.products.api.viewsets.routers')),
    path('expense/',include('apps.expense_manager.api.routers')),
    re_path('^swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$',serve,{
        'document_root': settings.MEDIA_ROOT, 
        }),
    ]