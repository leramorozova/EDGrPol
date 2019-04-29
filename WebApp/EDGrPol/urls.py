from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search_result', views.search_result, name='search_result'),
    path('alphabet', views.alphabet, name='alphabet'),
    path('failed_result', views.search_result, name='failed_result'),
    path('article/<int:pk>/', views.full_article, name='full_article'),
    path('materials', views.materials, name='materials'),
    path('team', views.team, name='team'),
    path('annotation', views.annotation, name='annotation'),
]
