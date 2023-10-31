from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_company, name='create_company'),

    path('edit/<int:company_id>/', views.edit_company, name='edit_company'),

    path('detail/<int:company_id>/', views.detail_company, name='detail_company'),
]
