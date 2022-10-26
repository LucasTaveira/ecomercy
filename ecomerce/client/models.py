from django.db import models

from authentication.models import User

class ClientManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=User.Type.CLIENT)
    
class Client(User):
    base_type = User.Type.CLIENT
    object = ClientManager()
    
    class Meta:
        proxy = True