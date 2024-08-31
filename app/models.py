from django.db import models

# Create your models here.

class sitemDamage(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = 'Sistema de Alerta'
        verbose_name_plural = 'Sistemas de Alertas'
    def __str__(self):
        return self.name
    
class sistemSelector(models.Model):
    sistema = models.ForeignKey(sitemDamage, related_name='sistema', on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)