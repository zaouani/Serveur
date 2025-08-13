from django.contrib import admin
from .models import Equipment, VariableData

class VariableDataInline(admin.TabularInline):
    model = VariableData
    extra = 1  # nombre de champs vides à afficher pour ajouter

class EquipmentAdmin(admin.ModelAdmin):
    inlines = [VariableDataInline]
    list_display = ('equipment_id',)

admin.site.register(Equipment, EquipmentAdmin)
