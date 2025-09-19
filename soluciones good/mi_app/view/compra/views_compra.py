from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from mi_app.models import *
from django.http import JsonResponse
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.urls import reverse_lazy
from mi_app.forms.form_compra import Compra




def listar_compra(request):
    data = {
        "titulo": "Listado de compras",
        "compra":Compra.objects.all()
    }
    return render(request, 'compra/compra.html', data)


class CompraListView(ListView):
    model = Compra
    template_name ='modulos/compra/compra.html'
    
    # @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        nombre = {'nombre' : 'Compra'}
        return JsonResponse(nombre)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de compras'
        context['crear_url'] = reverse_lazy('mi_app:compra_crear')
        context['entidad'] = 'Compra'  
        return context
    
class CompraCreateView(CreateView):
    model = Compra
    form_class = Compra
    template_name = 'modulos/compra/crear_compra.html'
    success_url = reverse_lazy('mi_app:compra_lista')
    
    def form_valid(self, form):
        messages.success(self.request, "compra creado correctamente")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['titulo'] = 'Crear compra'
        context ['entidad'] = 'compras'
        context ['listar_url'] = reverse_lazy('mi_app:compra_lista')
        return context
    
class CompraUpdateView(UpdateView):
    model = Compra
    form_class = Compra
    template_name = 'modulos/compra/crear_compra.html'
    success_url = reverse_lazy('mi_app:compra_lista')
    
    def form_valid(self, form):
        messages.success(self.request, "compra actualizado correctamente")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar compra'
        context['entidad'] = 'compras'
        context['listar_url'] = reverse_lazy('mi_app:compra_lista')
        return context

class CompraDeleteView(DeleteView):
    model = Compra
    template_name = 'modulos/compra/eliminar_compra.html'
    success_url = reverse_lazy('mi_app:compra_lista')
    
    def form_valid(self, form):
        messages.success(self.request, "compra eliminado correctamente")
        return super().form_valid(form)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar compra'
        context['entidad'] = 'compras'
        context['listar_url'] = reverse_lazy('mi_app:compra_lista')
        return context