from rest_framework import serializers

from seller.models import Seller
from address.serializers import AddressSerializer

class SellerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Seller
        fields = (
            'id',
            'seller_name',
            'cnpj',
            'username',
            'email',
            'password',
            'type',
            'address',
        )
        
    password = serializers.CharField(write_only=True, required=False)
    address = AddressSerializer(many=False, required=False)