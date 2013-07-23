from django.contrib import admin
from idiomas.models import Idioma


class IdiomaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Idioma, IdiomaAdmin)