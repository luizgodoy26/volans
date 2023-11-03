from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_item, name='create_item'),  

    path('list/', views.list_items, name='list_items'), 
    
    path('edit/<int:item_id>/', views.edit_item, name='edit_item'),  
    
    path('detail/<int:item_id>/', views.detail_item, name='detail_item'),  
    
]
