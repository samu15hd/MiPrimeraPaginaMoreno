from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from .forms import AutorForm
from .forms import CategoriaForm
from django.db.models import Q
from .forms import BusquedaForm

def lista_posts(request):
    posts = Post.objects.order_by('-fecha_publicacion')
    return render(request, 'lista_posts.html', {'posts': posts})

def detalle_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'detalle_post.html', {'post': post})

def crear_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_posts')
    return render(request, 'crear_post.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def crear_autor(request):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'crear_autor.html', {'form': form})

def crear_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'crear_categoria.html', {'form': form})

def buscar_posts(request):
    form = BusquedaForm(request.GET or None)
    resultados = []

    if form.is_valid():
        query = form.cleaned_data['query']
        resultados = Post.objects.filter(
            Q(titulo__icontains=query) |
            Q(contenido__icontains=query) |
            Q(autor__nombre__icontains=query) |
            Q(categoria__nombre__icontains=query)
        ).distinct()

    return render(request, 'buscar_posts.html', {'form': form, 'resultados': resultados})






