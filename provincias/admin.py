from django.contrib import admin
from provincias.models import Ciudad, CodigoPostal, Sector


class CiudadAdmin(admin.ModelAdmin):
    pass


class SectorAdmin(admin.ModelAdmin):
    pass


class CodigoPostalAdmin(admin.ModelAdmin):
    pass


admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(CodigoPostal,CodigoPostalAdmin)