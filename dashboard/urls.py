from django.urls import path
from . import views  # Certifique-se de que está importando as views corretamente

urlpatterns = [
    path('process_request/', views.process_request, name='process_request'),  # Definindo a URL para process_request
]