from django.urls import path
from . import views  # Certifique-se de importar sua view

urlpatterns = [
    path('process_request/', views.process_request, name='process_request'),  
]
