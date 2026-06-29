from django.db import transaction
from rest_framework import serializers
from .models import Category, Order, OrderItem, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'description', 'price', 'is_available']
        
        

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']
        
class OrderSerializer(serializers.ModelSerializer):
    # 1. bikin "laci" sementara namanya "items" buat nangkep list JSON dari frontend
    # write_only=True artinya cuma buat input, gak ditampilin pas output
    items = OrderItemSerializer(many=True, write_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'created_at', 'total_price', 'status', 'items']
        # 2. total_price kita kunci, biar  frontend gak bisa ngirim harga manual
        read_only_fields =  ['total_price', 'status']
        
    @transaction.atomic
    def create(self, validated_data):
        # 3. kita cabut "items" dari paket JSON utama
        items_data = validated_data.pop('items')
        
        # 4. kita bikin nota Order kosong (total_price masih default = 0)
        order = Order.objects.create(**validated_data)
        
        # 5. siapin variable penampung buat ngitung total harga
        calculated_total_price = 0
        
        for item_data in items_data:
            product = item_data['product'] # ini udah jadi objek Product (bukan ID lagi) berkat serializer
            quantity = item_data['quantity']
            
            # ambil harga
            original_price = product.price
            # simpen ke OrderItem
            OrderItem.objects.create(
                order = order,
                product = product,
                quantity = quantity,
                price_at_purchase = original_price
            )
            
            calculated_total_price += original_price * quantity
            
        
        
        # 6. terakhir, update total harga di nota Order dan save
        order.total_price = calculated_total_price
        order.save()
        return order