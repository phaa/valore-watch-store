from django.urls import path
from .views import index, user_data, orders, products, addresses, add_product
from .views import create_credit_card, show_credit_cards, edit_card, update_card, destroy_card

urlpatterns = [
    path('', index, name='user_index'),
    path('meusdados/', user_data, name='user_data'),
    path('pedidos/', orders, name='user_orders'),
    path('meusprodutos/', products, name='user_products'),
    path('meusprodutos/adicionarproduto/', add_product, name='user_add_product'),
    path('enderecos/', addresses, name='user_addresses'),

    path('meuscartoes/', create_credit_card, name='user_cards'),
    path('meuscartoes/cadastrar/', create_credit_card, name='create_card'),
    path('meuscartoes/editar/<uuid:id>', edit_card, name='edit_card'),
    path('meuscartoes/atualizar/<uuid:id>', update_card, name='update_card'),
    path('meuscartoes/apagar/<uuid:id>', destroy_card, name='destroy_card'),

]
