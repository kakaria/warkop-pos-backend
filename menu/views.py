from rest_framework import viewsets, filters, status # buat code (HTTP)
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Product, Order
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from .services import payment


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
    
    @action(detail=True, methods=['post'])
    def pay(self, request, pk=None):
        order = self.get_object()
        
        # jalanin function si ngecek apakah sudah bayar
        payment(order)
        
        return Response(
            {"message": "Payment success bro!"},
            status=status.HTTP_200_OK
        )
    
    