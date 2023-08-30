from django.urls import path

from . import views

urlpatterns = [
    # ex: localhost:8080/app/
    path('', views.index, name='index'),
    # ex: localhost:8080/app/sumar/18/19
    path('sumar/<int:a>/<int:b>/', views.add, name='add'),
    # ex: localhost:8080/app/restar/18/19
    path('restar/<int:a>/<int:b>/', views.subtract, name='subtract'),
    # ex: localhost:8080/app/multiplicar/18/19
    path('multiplicar/<int:a>/<int:b>/', views.multiply, name='multiply'),
]
