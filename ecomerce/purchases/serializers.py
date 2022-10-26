from rest_framework import serializers

from purchases.models import Purchases

class PurchasesSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Purchases
        fields = "__all__"