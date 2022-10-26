from rest_framework import serializers

from purchases.models import Purchases, ShoppingCart, ItensShoppingCart

class PurchasesSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Purchases
        fields = "__all__"
        
class ShoppingCartSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = ShoppingCart
        fields = "__all__"
        
class ItensShoppingCartSerializers(serializers.ModelSerializer):
        
    class Meta:
        model = ItensShoppingCart
        fields = "__all__"