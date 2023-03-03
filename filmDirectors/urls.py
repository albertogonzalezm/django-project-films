from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
    path('directores/', views.directors, name='directors'),
    path('film/<str:title>', views.film, name='filmDetail'),
    path('director/<str:name>', views.director, name='directorDetail'),
    path('add_film/', views.addfilm, name='addfilm'),
    path('add_director/', views.add_director, name='add_director')
]
