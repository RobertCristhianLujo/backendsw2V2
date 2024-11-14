from django.db import models
import datetime

# Create your models here.

class Producto(models.Model):
    productoName = models.CharField(max_length=200)
    productoDescription = models.CharField(blank=True, max_length=200)
    productoPrice = models.DecimalField(max_digits=10, decimal_places=2)
    productoImage = models.ImageField(null=True, blank=True, upload_to='images/')
    # create_at = models.DateTimeField(default=datetime.datetime.now)
    def __str__ (self):
        return self.productoName
    
class Cliente(models.Model):
    clienteName = models.CharField(max_length=200)
    clienteEmail = models.EmailField(max_length=200, blank=True, null=True)
    clientePhone = models.CharField(max_length=15, blank=True, null=True)
    clienteAddress = models.CharField(max_length=255, blank=True, null=True)
    clienteImage = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.clienteName
