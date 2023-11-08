from django.urls import path
from . import views

urlpatterns = [
    path('create_item/', views.create_item, name='create_item'),
    path('edit_item/<int:item_id>/', views.edit_item, name='edit_item'),
    path('detail_item/<int:item_id>/', views.detail_item, name='detail_item'),
    path('list_items/', views.list_items, name='list_items'),

    path('create_size/', views.create_size, name='create_size'),
    path('edit_size/<int:size_id>/', views.edit_size, name='edit_size'),
    path('list_sizes/', views.list_sizes, name='list_sizes'),


    path('create_category/', views.create_category, name='create_category'),
    path('edit_category/<int:category_id>/', views.edit_category, name='edit_category'),
    path('list_categories/', views.list_categories, name='list_categories'),


    path('create_stock/', views.create_stock, name='create_stock'),
    path('edit_stock/<int:stock_id>/', views.edit_stock, name='edit_stock'),
    path('list_stock/', views.list_stock, name='list_stock'),
]
