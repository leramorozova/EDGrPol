from django.urls import path
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('search_result', views.Search.as_view()),
    path('alphabet', views.Alphabet.as_view()),
    path('failed_result', views.Search.as_view()),
    path('article/<int:pk>/', views.WordEntry.as_view(), name="full_article"),
    path('materials', TemplateView.as_view(template_name="materials.html")),
    path('team', TemplateView.as_view(template_name="team.html")),
    path('annotation', TemplateView.as_view(template_name="annotation.html")),
    path('contacts', TemplateView.as_view(template_name="contacts.html")),
]
