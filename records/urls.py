from django.urls import path
from . import views


urlpatterns = [
    path('', views.book_list, name='list'),
    path('create/', views.book_create, name='create'),
    path('edit/<int:pk>', views.book_edit, name='edit'),
    path('delete/<int:pk>', views.book_del, name='del'),
    path('search/', views.api, name='search'),
]