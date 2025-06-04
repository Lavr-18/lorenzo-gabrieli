from django.urls import path
from . import views



urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('category/<int:category_id>/', views.products_by_category, name='products_by_category'),
]
