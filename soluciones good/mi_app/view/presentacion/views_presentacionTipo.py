from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from mi_app.models import *
from django.http import JsonResponse
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.urls import reverse_lazy
from mi_app.forms.form_presentacionTipo import presentacionTipoForm




def listar_presentacionTipo(request):
    data = {
        "titulo": "Listar Presentaciones",
        "presentaciones": PresentacionTipo.objects.all()
    }
    return render(request, 'presentacionTipo/presentacion.html', data)


class presentacionTipoListView(ListView):
    model = PresentacionTipo
    template_name ='modulos/PresentacionTipo/Presentacion.html'
    
    # @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        nombre = {'nombre' : 'listar Presentacioes'}
        return JsonResponse(nombre)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listar Presentaciones'
        context['crear_url'] = reverse_lazy('mi_app:presentacionTipo_crear')
        context['entidad'] = 'PresentacionTipo'  
        return context
    
class presentacionTipoCreateView(CreateView):
    model = PresentacionTipo
    form_class = presentacionTipoForm
    template_name = 'modulos/presentacionTipo/crear_presentacionTipo.html'
    success_url = reverse_lazy('mi_app:PresentacionTipo_lista')
    
    def form_valid(self, form):
        messages.success(self.request, "pesentacion  creada correctamente")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['titulo'] = 'Crear Presentacion'
        context ['entidad'] = 'PresentacionTipo'
        context ['listar_url'] = reverse_lazy('mi_app:presentacionTipo_lista')
        return context
    
class presentacionTipoupdateView(UpdateView):
    model = PresentacionTipo
    form_class = presentacionTipoForm
    template_name = 'modulos/presentacionTipo/crear_presentacionTipo.html'
    success_url = reverse_lazy('mi_app:presentacionTipo_lista')
    
    def form_valid(self, form):
        messages.success(self.request, "presentacion actualizada correctamente")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Presentacion'
        context['entidad'] = 'PresentacionTipo'
        context['listar_url'] = reverse_lazy('mi_app:presentacionTipo_lista')
        return context

class presentacionTipoDeleteView(DeleteView):
    model = PresentacionTipo
    template_name = 'modulos/presentacionTipo/eliminar_presentacionTipo.html'
    success_url = reverse_lazy('mi_app:presentacionTipo_lista')
    
    def form_valid(self, form):
        messages.success(self.request, "Presentacion eliminada correctamente")
        return super().form_valid(form)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Presentacion'
        context['entidad'] = 'PresentacionTipo'
        context['listar_url'] = reverse_lazy('mi_app:presentacionTipo_lista')
        return context