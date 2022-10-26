from django.contrib import admin
from django.urls import path, include
from django.db import router

from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from authentication.views import UserViewSet
from client.views import ClientViewSet
from product.views import ProductView
from seller.views import SellerViewSet
from purchases.views import PurchasesViewSet
from address.views import AddressViewSet

router = routers.DefaultRouter()

router.register(r'users', UserViewSet, basename='users')
router.register(r'clients', ClientViewSet, basename='clients')
router.register(r'products', ProductView, basename='products')
router.register(r'sellers', SellerViewSet, basename='sellers')
router.register(r'purchases', PurchasesViewSet, basename='purchases')
router.register(r'address', AddressViewSet, basename='address')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
