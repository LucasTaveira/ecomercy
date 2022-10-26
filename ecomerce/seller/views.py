from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from seller.models import Seller
from seller.serializers import SellerSerializer
from address.models import Address
from address.serializers import AddressSerializer

class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    
    def create(self, request, *args, **kwargs):
        validating_key = []
        user = request.data
        
        seller_data = {
            'seller_name': user.get('seller_name'),
            'cnpj': user.get('cnpj'),
            'username': user.get('username'),
            'email': user.get('email'),
            'password': user.get('password'),
            'type': user.get('type'),
        }
        
        seller_address_data = {
            "street": user.get('address.street'),
            "city": user.get('address.city'),
            "number": user.get('address.number'),
            "state": user.get('address.state'),
            "district": user.get('address.district'),
            "reference": user.get('address.reference') 
        }
        
        for k, v in seller_data.items():
            if v == '':
                validating_key.append(k)
                
        for k, v in seller_address_data.items():
            if v == '':
                validating_key.append(k)   
                
        if not validating_key:
            seller = Seller.object.create(**seller_data)
            instance = get_object_or_404(self.queryset, id=seller.id)
            instance.set_password('password')
            instance.save()
            
            address = Address.objects.create(**seller_address_data)
            address.save()
            instance.address = address
            instance.save()
        else:
            erro_dict={}
            for key in validating_key:
                erro_dict[key] = ' Campo obrigatório'
            
            return Response(erro_dict, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(
            SellerSerializer(
                instance, many=False).data, status=status.HTTP_200_OK)
        
    def update(self, request, *args, **kwargs):
        instance = get_object_or_404(self.queryset, id=kwargs.get('pk'))

        seller_data = {
            'seller_name': request.data.get('seller_name', instance.seller_name),
            'cnpj': request.data.get('cnpj', instance.cnpj),
            'username': request.data.get('username', instance.username),
            'email': request.data.get('email', instance.email),
            'type': request.data.get('type', instance.type),
        }
        
        if request.data.get('password'):
            instance.set_password(request.data.get('password'))
        
        seller_address_data = {
            "street": request.data.get(
                'address.street', instance.address.street),
            "city": request.data.get(
                'address.city', instance.address.city),
            "number": request.data.get(
                'address.number', instance.address.number),
            "state": request.data.get(
                'address.state', instance.address.state),
            "district":request.data.get(
                'address.district', instance.address.district),
            "reference": request.data.get(
                'address.reference', instance.address.reference)
        }
        
        seller_serializer = self.get_serializer(instance, data=seller_data)
        address_serializer = AddressSerializer(
            instance.address, data=seller_address_data)

        if seller_serializer.is_valid(raise_exception=True):
            seller_serializer.save()

        if address_serializer.is_valid(raise_exception=True):
            address_serializer.save()

                
        return Response(seller_serializer.data, status=status.HTTP_200_OK)