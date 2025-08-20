from django.urls import path
from .views import get_equipment, equipment_ids

urlpatterns = [
    path('equipment/<str:equipment_id>/', get_equipment, name='get_equipment'),
    path('equipment_ids/',equipment_ids, name='equipment_ids'),
]
