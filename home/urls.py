from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-property/', views.add_property, name='add_property'),
]