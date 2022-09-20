from django.contrib import admin
from Blog.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.



#CLASES HEREDADAS DE APP DE TERCERO "IMPORT EXPORT"
class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor

class PostResource(resources.ModelResource):
    class Meta:
        model = Post

#CLASES PROPIAS DE ADMIN PARA CONFIGURAR CAMPOS DE BUSQUEDA Y TITULOS DE LOS MODELOS


class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    #Creo un campo de busqueda para buscar las categorías por nombre.
    search_fields = ['nombre']
    list_display = ('nombre','estado','fecha',)

class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombres','apellidos']
    list_display = ('nombres','apellidos','correo','fecha_creacion','estado',)

class PostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['titulo']
    list_display = ('titulo','estado','fecha_creacion',)


# REGISTROS DE DIFERENTES MODELOS PARA SU CORRECTA VISUALIZACIÓN EN EL ADMIN
#Registramos Categoría y CategoríaAdmin
admin.site.register(Categoria,CategoriaAdmin)

#Nuevamente registramos tambien nuestra clase AutorAdmin en este caso.
admin.site.register(Autor,AutorAdmin)

#Registro mi Post
admin.site.register(Post,PostAdmin)
