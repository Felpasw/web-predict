from django.urls import path
from . import views

urlpatterns = [
    path('', views.average_data_view, name='average_data_view'),
    path('analisar-csv/', views.analisar_csv, name='analisar_csv'),
    path('mapa_casas/', views.mapa_casas, name='mapa_casas'),
    path("uploads", views.upload_csv, name="upload_csv"),
    path('retrain_base/', views.retrain_base, name='retrain_base'),


]
