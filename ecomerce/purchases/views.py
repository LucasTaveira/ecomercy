from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from authentication.models import User
from purchases.models import Purchases
from purchases.serializers import PurchasesSerializers

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