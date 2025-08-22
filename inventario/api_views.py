from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by('-fecha_creacion')
    serializer_class = ProductoSerializer # Usa el serializador ProductoSerializer para convertir objetos Producto a JSON
    permission_classes = [IsAuthenticated] # Solo usuarios autenticados pueden acceder
