from django.contrib import admin
# Register your models here.
from api.models import Cliente, Producto

admin.site.register(Producto)
admin.site.register(Cliente)
