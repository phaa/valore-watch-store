from django.urls import path
from .views import index, user_data, orders, products, cards, addresses, add_product

urlpatterns = [
    path('', index, name='user_index'),
    path('meusdados/', user_data, name='user_data'),
    path('pedidos/', orders, name='user_orders'),
    path('meusprodutos/', products, name='user_products'),
    path('meusprodutos/adicionarproduto/', add_product, name='user_add_product'),
    path('meuscartoes/', cards, name='user_cards'),
    path('enderecos/', addresses, name='user_addresses'),
]
