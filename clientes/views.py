from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status

from clientes.models import Cliente
from clientes.serializers import ClienteSerializer

#lista de clientes
@api_view(['GET'])
def index(request):
    clientes = Cliente.objects.all()
    serializer = ClienteSerializer(clientes, many=True)
    return Response(serializer.data)
    
@api_view(['POST'])
def store(request):
    serializer = ClienteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

