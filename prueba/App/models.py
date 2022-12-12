from django.db import models

# Create your models here.
class familiares(models.Model):
    nombre=models.CharField(max_length=50)#este es el str
    edad=models.IntegerField()
    fn=models.DateField()

    def __str__(self):
        return self.nombre