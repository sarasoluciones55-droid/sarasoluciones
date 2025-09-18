from django.shortcuts import render
from mi_app.models import *
from django.urls import reverse_lazy





def listar_principal(request):
    data = {
        "titulo": "pagina principal",
    }
    return render(request, 'principal/principal.html', data)