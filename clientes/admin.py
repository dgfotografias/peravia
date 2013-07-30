from django.contrib import admin
from clientes.models import Cliente, Idioma, Ciudad, CodigoPostal, TipoCliente,Observaciones
#from django import forms
#from django.forms.models import BaseInlineFormSet
#from django.core.exceptions import ValidationError
#from django.forms.formsets import BaseFormSet

"""
class BaseClienteFormSet(BaseInlineFormSet):

    def clean(self):
        super(BaseClienteFormSet, self).clean()

        if any(self.errors):
            return
        cliente = []
        for i in range(0, self.total_form_count()):
            form = self.forms[i]
            cliente = form.cleaned_data['cliente']

            if cliente == 2:
                raise forms.ValidationError("Error cliente")
            cliente.append(cliente)

"""

"""
class ExtraInfoClienteInline(admin.StackedInline):
    model = ExtraInfoCliente
    max_num = 1
    #formset = BaseClienteFormSet
"""


class ClienteAdmin(admin.ModelAdmin):
    date_hierarchy = 'fecha'
    list_display = ('nombre', 'apellidos', 'cliente','ciudad','get_id')
    list_filter = ('cliente__cliente','sexo')
    search_fields =['nombre','apellidos','email','ciudad__ciudad','telefono','dni']



   # inlines = [
   #     ExtraInfoClienteInline,

   #]
    """
    def get_formsets(self, request, obj=None):
        for inline in self.get_inline_instances(request, obj):
            # hide MyInline in the add view
            if isinstance(inline, ExtraInfoClienteInline) and obj is None:
                continue
            yield inline.get_formset(request, obj)



    def clean_name(self):
        if self.cleaned_data.get("cliente") == 2:
            raise forms.ValidationError("Error")
        else:
            return self.cleaned_data.get("cliente")
    """





class TipoClienteAdmin(admin.ModelAdmin):
    pass

class ObservacionesClienteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(TipoCliente, TipoClienteAdmin)
admin.site.register(Observaciones, ObservacionesClienteAdmin)
