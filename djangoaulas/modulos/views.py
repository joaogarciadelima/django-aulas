from django.shortcuts import render
#
# # Create your views here.
from djangoaulas.modulos import facade


def detalhe(request, slug):
    modulo = facade.encontrar_modulo(slug)
    return render(request, 'modulos/modulo_detalhe.html', {'modulo': modulo})
