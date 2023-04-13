from django.urls import path
from .views import listar_item, criar_item, update_item, deletar_item

urlpatterns = [
    path('', listar_item, name='listar_item'),
    path('new', criar_item, name='criar_item'),
    path('update/<int:id>/', update_item, name='update_item'),
    path('delete/<int:id>/', deletar_item, name='deletar_item'),
]