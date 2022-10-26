from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.db import router

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,
)

from authentication.views import UserViewSet
from client.views import ClientViewSet
from product.views import ProductView
from seller.views import SellerViewSet
from purchases.views import (
    PurchasesViewSet, ShoppingCartViewSet, ItensShoppingCartViewSet
)
from address.views import AddressViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()

router.register(r'users', UserViewSet, basename='users')
router.register(r'clients', ClientViewSet, basename='clients')
router.register(r'products', ProductView, basename='products')
router.register(r'sellers', SellerViewSet, basename='sellers')
router.register(r'purchases', PurchasesViewSet, basename='purchases')
router.register(r'address', AddressViewSet, basename='address')
router.register(r'shoppingcart', ShoppingCartViewSet, basename='shoppingcart'),
router.register(r'itens/shoppingcart', ItensShoppingCartViewSet, basename='istens_shoppingcart')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
