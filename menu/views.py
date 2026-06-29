from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Product, Order
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    # 1. tentuin datanya (ngambil data dari mana)
    queryset = Category.objects.all()
    
    # 2. panggil serializernya (penerjemahnya)
    serializer_class = CategorySerializer
    
    # 3. pasang satpam
    permission_classes = [IsAuthenticated]
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    
    serializer_class = ProductSerializer
    
    permission_classes = [IsAuthenticated]
    
    # pasang mesin pencari di dalam list
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    
    # tentuin kolom yang mau dicari  (pake list of string)
    search_fields = ['name', 'description']
    
    # tentuin kolom yang butuh presisi tinggi (exact match)
    filterset_fields = ['category', 'is_available']
    
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.prefetch_related('order_items').all()
    
    serializer_class = OrderSerializer
    
    permission_classes = [IsAuthenticated]
    
    