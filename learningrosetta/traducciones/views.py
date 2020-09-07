'''
Prueba de documentación docstring Sphinx
'''
# from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _


# Create your views here.
def traducciones_list(request):
    output = _('Bienvenido a las traducciones')
    return HttpResponse(output)
