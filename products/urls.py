from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


urlpatterns = [
    path('products/', views.products , name='products'),
    path('add_products/', views.products_create , name='add_products'),
    path('update_prod/<int:id>', views.update_products, name='update_products'),
    path('delete_prod/<int:id>', views.delete_products, name='delete_products'),
    path('add_quatation/', views.add_quatation, name='add_quatation'),
    path('view_quatation/', views.quatation, name='quatation'),
    url(r'^search_jwel/$', views.search_jwel, name='search_jwel'),


]