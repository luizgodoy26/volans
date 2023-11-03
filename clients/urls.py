from django.urls import path
from . import views

urlpatterns = [
    
    #Currently set as home page ''
    path('', views.list_clients, name='list_clients'),

    path('create/', views.create_client, name='create_client'),

    path('list/', views.list_clients, name='list_clients'),

    path('edit/<int:client_id>/', views.edit_client, name='edit_client'),

    path('detail/<int:client_id>/', views.detail_client, name='detail_client'),
]
