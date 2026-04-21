from django.shortcuts import render, redirect
from .forms import CurriculoForm
from .models import Curriculo

def criar_curriculo(request):
    if request == "POST":
        form = CurriculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_curriculos')
        
    else:
        form = CurriculoForm()
        return render(request, 'curriculos/form.html', {'form':form})
    
def lista_curriculos(request):
    curriculos = Curriculo.objects.all()
    return render(request, 'curriculos/lista.html', {'curriculos': curriculos})



