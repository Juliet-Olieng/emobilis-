from django.urls import path
from .views import ProductDetailView
from .views import ProductListView

urlpatterns=[
     path('products/',ProductListView.as_view(),name='product_list_view'),
    path('product/<int:id>/',ProductDetailView.as_view(), name='product_detail_view'),
]