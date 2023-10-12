from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Titulo')
    description = models.TextField(verbose_name = 'Descripcion')
    
    link = models.URLField(verbose_name = 'Direccion web', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de edicion')
    

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        
    def __str__(self):
        return self.title
    
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(verbose_name = 'Imagen', upload_to='project')
    description = models.TextField(verbose_name='Descripcion', blank=True, null=True)

    class Meta:
        verbose_name = 'Imagen del Proyecto'
        verbose_name_plural = 'Imagenes del Proyecto'

    def __str__(self):
        return f"Imagen para {self.project.title}"