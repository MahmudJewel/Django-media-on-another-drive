from django.urls import path, include
from .views import product_list, product_view, create_product, update_product
urlpatterns = [
    path('', product_list, name="home"),
    path('product/<int:pk>/', product_view, name="product_view"),
    path('product/create/', create_product, name="create_product"),
    path('update/<int:pk>/', update_product, name="update_product"),

]
