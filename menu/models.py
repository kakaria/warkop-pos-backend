from django.db import models
 
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)
    # bikin foreign key
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    
    
    def __str__(self):
        return self.name
    
    
    
class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField(default=0)
    
    def __str__(self):
        return f"Order has been created at #{self.created_at.strftime('%Y-%m-%d %H:%M')}"
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_items')
    quantity = models.IntegerField()
    price_at_purchase = models.IntegerField()
    
    def __str__(self):
        return f"{self.quantity} x{self.product.name}"
    
