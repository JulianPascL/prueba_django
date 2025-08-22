Proyecto Django: prueba_django

Este proyecto es una aplicación web construida con Django que permite registrar y listar productos, con autenticación de usuarios y una API REST protegida.

# CARACTERISTICAS
- Modelo Producto con validaciones.
- Autenticación de usuarios (login/logout).
- Página de inicio con tabla de productos y formulario para agregar.
- API REST con Django REST Framework.
- Paginación en el listado.
- Validación de precio positivo.

# REQUISITOS

- Python 3.10 o superior
- Django 5.x
- Django REST Framework

# INSTALACION

1. Clona el repositorio
2. En la terminal, define las dependencias
      --> pip install django djangorestframework
3. En la terminal, define las migraciones
       --> python manage.py makemigrations
       --> python manage.py migrate
4. En terminal, crea un superusuario:
       --> python manage.py createsuperuser
   *USUARIO PRUEBA*
         user: admin
         password: admin123
6. Ejecuta el servidor:
       --> python manage.py runserver
 
Accede a la aplicación:

Inicio:  http://127.0.0.1:8000/ 
Login:  http://127.0.0.1:8000/accounts/login/ 
Admin:  http://127.0.0.1:8000/admin/ 
API:  http://127.0.0.1:8000/api/productos/ 

