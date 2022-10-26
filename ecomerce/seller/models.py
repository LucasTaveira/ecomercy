from django.db import models

from authentication.models import User

class SellerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=User.Type.SELLER)
    
class Seller(User):
    base_type = User.Type.SELLER
    object = SellerManager()
    
    class Meta:
        proxy = True