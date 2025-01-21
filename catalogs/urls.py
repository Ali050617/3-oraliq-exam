from django.urls import path
from . import views


app_name = 'catalog'

urlpatterns = [
    path('list/', views.catalog_list, name='catalog_list'),
    path('detail/<int:catalog_id>/', views.catalog_detail, name='catalog_detail'),
]

