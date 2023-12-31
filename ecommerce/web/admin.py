from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import Categoria,Marca,Producto

admin.site.register(Categoria)
admin.site.register(Marca)
#admin.site.register(Producto)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    
    def imagen_html(self,obj):
        return format_html('<img src="{}" width=150px />'.format(obj.imagen.url))
    
    imagen_html.short_description = 'Image'
    
    list_display = ('categoria','marca','nombre','precio','imagen_html')
    list_editable = ('precio',)
    list_filter = ('categoria','marca',)