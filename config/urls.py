from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('products/', include('products.urls')),
    path('users/', include('users.urls', namespace='users')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('account/', include('accounts.urls', namespace='accounts')),
    # path('account/', include('users.urls', namespace='users')),


]
