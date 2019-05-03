from django.urls import include, path, re_path
from . import views

app_name = 'products'

urlpatterns = [
    path('products/',
        views.GetOrCreateProductView.as_view(),
        name='get_or_create_product'
    ),
    
    path('products/<int:pk>',
        views.GetUpdateOrDeleteProductView.as_view(),
        name='product_get_update_or_delete'
    ),
    path('items', views.get_item, name='items')
]