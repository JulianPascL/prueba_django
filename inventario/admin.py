from django.contrib import admin
from .models import Producto

#Gestionar productos desde el panel de administración
admin.site.register(Producto)
