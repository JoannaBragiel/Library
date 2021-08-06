from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.apiOverview, name='api-overview'),
    path('api_book_list/', views.api_book_list, name="api_book_list"),
    path('api_book_detail/<int:pk>/', views.api_book_detail, name="api_book_detail"),
    path('api_book_create/', views.api_book_create, name="api_book_create"),
    path('api_book_update/<int:pk>/', views.api_book_update, name="api_book_update"),
    path('api_book_delete/<int:pk>/', views.api_book_delete, name="api_book_delete"),
]