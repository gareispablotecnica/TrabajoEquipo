from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Especialidad, Noticia


def home(request):
    context = {
        'especialidades': Especialidad.objects.filter(activa=True),
        'noticias': Noticia.objects.filter(publicada=True)[:3],
    }
    return render(request, 'home.html', context)


@login_required
def bienvenida(request):
    return render(request, 'bienvenida.html')
