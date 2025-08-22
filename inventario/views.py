from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Producto
from .forms import ProductoForm
from django.core.paginator import Paginator

@login_required # Requiere que el usuario esté autenticado para acceder a la vista
def index(request):
    productos = Producto.objects.all().order_by('-fecha_creacion')
    paginator = Paginator(productos, 5)
    page = request.GET.get('page')
    productos_paginados = paginator.get_page(page)
    return render(request, 'index.html', {'productos': productos_paginados})

@login_required
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductoForm()
    return render(request, 'agregar.html', {'form': form})
