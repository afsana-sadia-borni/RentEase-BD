from django.urls import path
from . import views

urlpatterns = [
 proma-working-code
    path('', views.home, name='home'),
    path('add-property/', views.add_property, name='add_property'),

    path('', views.property_list_view, name='property_list'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
 main
]