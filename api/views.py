from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Equipment
from .serializers import EquipmentSerializer

@api_view(['GET'])
def get_equipment(request, equipment_id):
    try:
        equipment = Equipment.objects.get(equipment_id=equipment_id)
    except Equipment.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)

    serializer = EquipmentSerializer(equipment)
    return Response(serializer.data)
