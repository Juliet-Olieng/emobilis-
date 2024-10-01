from django.urls import path
from.views import upload_product
from.views import product_list
from.views import product_detail
from.views import add_to_cart
from.views import edit_product_view
from .views import remove_product_from_cart

urlpatterns = [
    path("products/upload",upload_product,name="product_upload_view"),
    path("products/list",product_list,name="product_list_view"),
    path("products/<int:id>/",product_detail,name="product_detail_view"),
    path("products/edit/<int:id>/",edit_product_view,name="edit_product_view"),
    path('add_to_cart/<int:id>/', add_to_cart, name='add_to_cart'),
    path('remove_product/<int:basket_id>/<int:product_id>/',remove_product_from_cart, name='remove_product'),
]
