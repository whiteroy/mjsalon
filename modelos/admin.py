from django.contrib import admin
from .models import Usuarios, Empresa, Cliente, Proveedor

# Register your models here.

admin.site.register(Usuarios)
admin.site.register(Empresa)
admin.site.register(Cliente)
admin.site.register(Proveedor)