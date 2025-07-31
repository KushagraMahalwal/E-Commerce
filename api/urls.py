from django.urls import path
from .views import (
    CartDeleteView, CartListCreateView, CategoryListCreateView, CategoryDetailView, OrderListView, PlaceOrderView,
    ProductListCreateView, ProductDetailView, UpdateOrderStatusView
)

urlpatterns = [
    # Categories
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    # Products
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    path('cart/', CartListCreateView.as_view(), name='cart'),
    path('cart/<int:pk>/', CartDeleteView.as_view(), name='cart-delete'),
    path('order/place/', PlaceOrderView.as_view(), name='place-order'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/status/', UpdateOrderStatusView.as_view(), name='update-order-status'),
]
