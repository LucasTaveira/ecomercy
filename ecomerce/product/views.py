from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from authentication.models import User
from product.models import Product
from product.serializers import ProductSerializer

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
            
    def create(self, request, *args, **kwargs):

        return super().create(request, *args, **kwargs)
        #     else:
        #         return Response(
        #             data={'detail':'Acesso Negado'}, 
        #             status=status.HTTP_401_UNAUTHORIZED)
        # except:
        #     return Response(
        #         data={'detail': 'Necessário logar para cadastrar produtos'},
        #         status=status.HTTP_401_UNAUTHORIZED)
            
    def update(self, request, *args, **kwargs):
        
        try:
            if self.request.user.type == User.Type.SELLER and request.user.id == self.request.user.id:
                return super().update(request, *args, **kwargs)
            else:
                return Response(
                    data={'detail':'Acesso Negado'}, 
                    status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response(
                data={'detail': 'Necessário logar para cadastrar produtos'},
                status=status.HTTP_401_UNAUTHORIZED)
            
    def destroy(self, request, *args, **kwargs):
        try:
            if self.request.user.type == User.Type.SELLER and request.user.id == self.request.user.id:
                return super().destroy(request, *args, **kwargs)
            else:
                return Response(
                    data={'detail':'Acesso Negado'}, 
                    status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response(
                data={'detail': 'Necessário logar para cadastrar produtos'},
                status=status.HTTP_401_UNAUTHORIZED)