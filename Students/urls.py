from django.urls import path
from . import views

urlpatterns = [
    path('list', views.List.as_view()),
    path('add', views.Add.as_view()),
]