from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_client, name='create_client'),

    path('edit/<int:client_id>/', views.edit_client, name='edit_client'),

    path('detail/<int:client_id>/', views.detail_client, name='detail_client'),
]
