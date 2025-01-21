from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('list/', views.author_list, name='author_list'),
    path('detail/<int:author_id>/', views.author_detail, name='author_detail'),
]

