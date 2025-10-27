from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.lista_posts, name='lista_posts'),
    path('post/', views.crear_post, name='crear_post'),
    path('post/<int:post_id>/', views.detalle_post, name='detalle_post'),
    path('autor/', views.crear_autor, name='crear_autor'),
    path('categoria/', views.crear_categoria, name='crear_categoria'),
    path('buscar/', views.buscar_posts, name='buscar_posts'),
]


