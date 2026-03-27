from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api_views, views

router = DefaultRouter()
router.register(r'categories', api_views.CategoryViewSet)
router.register(r'products', api_views.ProductViewSet)

# API URLs
api_urlpatterns = [
    path('', include(router.urls)),
    path('cart/', api_views.cart_detail, name='api-cart-detail'),
    path('cart/add/', api_views.cart_add, name='api-cart-add'),
    path('cart/update/<int:item_id>/', api_views.cart_update, name='api-cart-update'),
    path('cart/remove/<int:item_id>/', api_views.cart_remove, name='api-cart-remove'),
    path('checkout/', api_views.checkout, name='api-checkout'),
    path('orders/', api_views.order_list, name='api-order-list'),
    path('orders/<int:order_id>/', api_views.order_detail, name='api-order-detail'),
]

# UI URLs
urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product-list'),
    path('products/<slug:slug>/', views.product_detail, name='product-detail'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('orders/', views.order_list_view, name='orders'),
    path('orders/<int:order_id>/', views.order_detail_view, name='order-detail'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
