from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, OrderViewSet

# 1. panggil mesin Route
route = DefaultRouter()

# 2. daftarin ruangan manajernya ke resepsionis router
route.register('categories', CategoryViewSet)
route.register('products', ProductViewSet)
route.register('orders', OrderViewSet)


# 3. ekspor URLnya biar bisa dibaca sama Django
urlpatterns = [
    path('', include(route.urls)),
]