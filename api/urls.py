from django.urls import path
from .views import get_equipment

urlpatterns = [
    path('equipment/<str:equipment_id>/', get_equipment, name='get_equipment'),
]
