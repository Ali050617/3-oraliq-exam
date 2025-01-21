from django.urls import path
from . import views


app_name = 'tags'

urlpatterns = [
    path('tags', views.tag_list, name='tag_list'),
    path('detail/<int:tag_id>/', views.tag_detail, name='tag_detail'),
]

