from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titulo") #Charfield = varchar
    content = RichTextField(verbose_name="Contenido") #Textfield para text-areas
    slug= models.CharField(unique=True,max_length=150, verbose_name="Url amigable")
    visible= models.BooleanField(verbose_name="¿Visible?")
    order = models.IntegerField(default=0,verbose_name="Orden")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creacion:") 
    updated_at=  models.DateTimeField(auto_now_add=True, verbose_name="Actualización:")
    class Meta:
        #poner nombre en singular
        verbose_name="Pagina"
        verbose_name_plural= "Paginas"
    def __str__(self):
        return self.title