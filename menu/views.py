from rest_framework import viewsets, filters, status # buat code (HTTP)
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
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
    
    @action(detail=True, methods=['post'])
    def pay(self, request, pk=None):
        # 1. ambil data nota spesifik berdasarkan id (pk) yang dikasih user
        order = self.get_object()
        
        # 2. logika bisnis (cegah bayar 2 kali)
        if order.status == 'PAID':
            return Response(
                {'error': f'Bos! order dengan id {order.id} ini udah dibayar loh!'},
                status=status.HTTP_400_BAD_REQUEST
            )
        order.status = 'PAID'      
        order.save()
        
        return Response(
            {'message': f'sukses! Nota nomor {order.id} berhasil dibayar'},
            status=status.HTTP_200_OK
        )
    
    