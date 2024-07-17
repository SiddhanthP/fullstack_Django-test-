from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('generate-csv/', views.generate_csv_view, name='generate_csv'),
    path('generate-pdf/', views.generate_pdf_view, name='generate_pdf'),
]

