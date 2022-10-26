from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authentication.models import User
from purchases.models import (
    Purchases, ShoppingCart, ItensShoppingCart
)
from purchases.serializers import (
    PurchasesSerializers, ShoppingCartSerializers, ItensShoppingCartSerializers
)

class PurchasesViewSet(viewsets.ModelViewSet):
    queryset = Purchases.objects.all()
    serializer_class = PurchasesSerializers
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.type == User.Type.CLIENT:
            return Purchases.objects.filter(client_id=user.id)
        if user.type == User.Type.SELLER:
            return Purchases.objects.filter(seller_id=user.id)
            
class ItensShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ItensShoppingCart.objects.all()
    serializer_class = ItensShoppingCartSerializers
    # permission_classes = [IsAuthenticated]
    
    # def get_queryset(self):
    #     user = self.request.user
    #     if user.type == User.Type.CLIENT:
    #         return ItensShoppingCart.objects.filter(client_id=user.id)

class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializers
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.type == User.Type.CLIENT:
            return ShoppingCart.objects.filter(
                itens_shoppingcart__client_id=user.id)
          
    def create(self, request, *args, **kwargs):

        try:
            if self.request.user == User.Type.CLIENT:
                final_value = 0
                itens = ItensShoppingCart.objects.filter(
                    id__in=request.data.get('itens_shoppingcart'))
                
                for i in itens:
                    final_value = final_value+(i.product.value*i.qty)
                shoppingcart = super().create(request, *args, **kwargs)
                instance = ShoppingCart.objects.get(
                    id=shoppingcart.data.get('id'))
                instance.value=final_value
                instance.save()

                return Response(ShoppingCartSerializers(
                    shoppingcart, many=False).data,
                    status=status.HTTP_200_OK)
            else:
                return Response(
                    data={
                        'detail':'Acesso Negado.'},
                    status=status.HTTP_401_UNAUTHORIZED)

        except:
            return Response(
                data={
                    'detail':'Erro na solicitação, verifique as informações fornccidas.'},
                status=status.HTTP_400_BAD_REQUEST)
