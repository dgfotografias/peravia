from django.contrib import admin

from todo.models import ToDo


class ToDoAdmin(admin.ModelAdmin):
    fields = ['fecha', 'titulo','description', 'cliente', 'finalizada']
    list_display = ('titulo', 'fecha', 'cliente','finalizada')
    list_filter = ['fecha', 'finalizada']
    search_fields = ['cliente','titulo']

admin.site.register(ToDo,ToDoAdmin)