from django.urls import path

from . import views

urlpatterns = [
    path('', views.traducciones_list, name='traducciones_list'),
]
