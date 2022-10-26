from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from authentication.models import User
from product.models import Product
from product.serializers import ProductSerializer

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        
        if user.type == User.Type.SELLER:
            return Product.objects.filter(seller_id=user.id)

        
    def create(self, request, *args, **kwargs):

        if self.request.user.type == User.Type.SELLER:
            return super().create(request, *args, **kwargs)
        else:
            return Response(
                data={'detail':'Acesso Negado'}, 
                status=status.HTTP_401_UNAUTHORIZED)