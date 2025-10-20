MiPrimeraPagina+Moreno
=======================

Este proyecto es una aplicación web de blog desarrollada con Django como parte de la Preentrega 3 del curso de Python de Coderhouse.

INSTALACIÓN
-----------

1. Cloná el repositorio o descargalo como ZIP.
2. Abrí una terminal en la carpeta del proyecto.
3. Creá y activá un entorno virtual:
   python -m venv entorno_virtual
   .\entorno_virtual\Scripts\activate
4. Instalá las dependencias:
   pip install -r requirements.txt
5. Aplicá las migraciones:
   python manage.py makemigrations
   python manage.py migrate
6. Iniciá el servidor:
   python manage.py runserver

FUNCIONALIDADES
---------------

- Registro y listado de autores
- Registro y listado de categorías
- Creación y visualización de publicaciones
- Subida opcional de imágenes en los posts
- Búsqueda por título, contenido, autor y categoría
- Navegación con herencia de plantilla base.html

CÓMO PROBAR
-----------

1. Ingresá a http://localhost:8000/
2. Crear autores desde /autor/
3. Crear categorías desde /categoria/
4. Crear publicaciones desde /post/
5. Ver publicaciones en /posts/
6. Buscar contenido desde /buscar/

ESTRUCTURA DEL PROYECTO
------------------------

- models.py: Define los modelos Autor, Post, Categoria
- forms.py: Formularios para cada modelo y búsqueda
- views.py: Lógica para crear, listar y buscar contenido
- templates/: HTML con Bootstrap y herencia de diseño
- urls.py: Rutas de la aplicación

REQUISITOS CUMPLIDOS
--------------------

- Proyecto Django con patrón MVT
- Herencia de plantilla base
- Tres modelos definidos
- Formularios para insertar datos
- Búsqueda en la base de datos
- Página principal funcional
- README explicativo

AUTOR
-----

Samuel Moreno  
Curso Python — Coderhouse  
Preentrega 3
