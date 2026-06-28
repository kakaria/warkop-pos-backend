from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
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
    
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.prefetch_related('order_items').all()
    
    serializer_class = OrderSerializer
    
    permission_classes = [IsAuthenticated]
    
    