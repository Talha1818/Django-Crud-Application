from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add', views.ADD, name='add'),
    path('edit', views.EDIT, name='edit'),
    path('update/<str:id>', views.UPDATE, name='update'),
    path('delete/<str:id>', views.DELETE, name='delete'),
]
