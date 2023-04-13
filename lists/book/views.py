from django.shortcuts import render, redirect
from .models import Item
from .forms import ItensForm

# Create your views here.

def listar_item(request):
    itens = Item.objects.all()
    return render(request, 'lists/itens.html', {'itens': itens})


def criar_item(request):
    form = ItensForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_item')

    return render(request, 'lists/cadastroitem.html', {'form': form})


def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItensForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('listar_item')

    return render(request, 'lists/cadastroitem.html', {'form': form, 'item': item})


def deletar_item(request, id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('listar_item')

    return render(request, 'lists/cadastroitem.html', {'item': item})