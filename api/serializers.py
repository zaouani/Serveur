from rest_framework import serializers
from .models import Equipment, VariableData

class VariableDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariableData
        fields = ['name', 'valeur', 'unite', 'classe']

class EquipmentSerializer(serializers.ModelSerializer):
    variables = VariableDataSerializer(many=True)
    lastDecodeTime = serializers.FloatField( default=0.0)
    class Meta:
        model = Equipment
        fields = ['equipment_id','lastDecodeTime', 'variables']