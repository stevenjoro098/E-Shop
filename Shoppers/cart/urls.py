from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),  # products  LIST
    path('add/<int:pk>', views.cart_add, name='cart_add'),
    path('clear/', views.cart_clear, name='cart_clear'),
    path('remove/<int:pk>', views.cart_remove, name='cart_remove'),
]