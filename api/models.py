from django.db import models

class Equipment(models.Model):
    equipment_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.equipment_id

class VariableData(models.Model):
    equipment = models.ForeignKey(Equipment, related_name='variables', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    valeur = models.FloatField()
    unite = models.CharField(max_length=20)
    classe = models.IntegerField()
