from django.urls import path
from . import views

urlpatterns = [
    path('', views.average_data_view, name='average_data_view'),
]
