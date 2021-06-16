
from django.urls import path
from . import views

app_name = 'Shop'

urlpatterns = [
    path('products', views.ProductList.as_view(), name='productlist'),  # products  LIST
    path('products/<int:pk>', views.ProductDetail.as_view(), name='productdetails'),
    path('products/<int:pk>', views.product_detail, name='productdetails'),# Product Details
    path('<int:id>/<slug>', views.product_detail, name='product_detail'),
    path('products/api/v1', views.ProductApiView.as_view()),
    path('products/api/v1/reference', views.reference_code, name='reference_code')
]
