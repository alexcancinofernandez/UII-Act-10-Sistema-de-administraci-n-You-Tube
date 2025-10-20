from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_video, name='add_video'),
    path('edit/<int:id>/', views.edit_video, name='edit_video'),
    path('delete/<int:id>/', views.delete_video, name='delete_video'),
]
