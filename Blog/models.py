from ensurepip import version
from pyexpat import model
from tabnanny import verbose
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de Categoria' , max_length=100,null=False,blank=False)
    estado = models.BooleanField('Categoria Activada/Categoria No Activada', default=True)
    fecha = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombres del Autor',max_length=100,null=False,blank=False)
    apellidos = models.CharField('Apellidos del Autor',max_length=100,null=False,blank=False)
    facebook = models.URLField('Facebook',null=True,blank=True)
    instagram = models.URLField('Instagram',null=True,blank=True)
    twiter = models.URLField('Twiter',null=True,blank=True)
    pagina = models.URLField('Página Web',null=True,blank=True)
    correo = models.EmailField('Correo Electrónico', null=False,blank=False)
    estado = models.BooleanField('Autor Activo/ Autor No Activo', default=True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False,auto_now_add=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return f' {self.apellidos}  {self.nombres} '

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=150,null=False,blank=False)
    slug = models.CharField('Slug', max_length=150,null=False,blank=False)
    descripcion = models.CharField('Descripcion', max_length=250,null=False,blank=False)
    imagen = models.URLField(max_length=255,null=False,blank=False)
    contenido = RichTextField()
    autor = models.ForeignKey(Autor,on_delete= models.CASCADE)
    categoria = models.ForeignKey(Categoria,on_delete= models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado',default=True)
    fecha_creacion = models.DateField('Fecha de Creacion',auto_now=False,auto_now_add=True )

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo

