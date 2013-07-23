from django.contrib import admin

from vehiculos.models import Vehiculo,Marca,Modelo,Color, Neumatico, Lubricante, Bateria, Tipo

class VehiculoAdmin(admin.ModelAdmin):
    pass

class MarcaAdmin(admin.ModelAdmin):
    pass

class ModeloAdmin(admin.ModelAdmin):
    pass

class TipoAdmin(admin.ModelAdmin):
    pass


class ColorAdmin(admin.ModelAdmin):
    pass


class NeumaticoAdmin(admin.ModelAdmin):
    pass


class LubricanteAdmin(admin.ModelAdmin):
    pass


class BateriaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Vehiculo, VehiculoAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Modelo, ModeloAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Neumatico, NeumaticoAdmin)
admin.site.register(Lubricante, LubricanteAdmin)
admin.site.register(Bateria, BateriaAdmin)
admin.site.register(Tipo,TipoAdmin)