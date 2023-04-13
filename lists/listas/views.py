from django.shortcuts import render
from .models import Lista

# Create your views here.

def index(request):
    return render(request, "listas/produto.html", {
        "listas": Lista.objects.all()
    })


