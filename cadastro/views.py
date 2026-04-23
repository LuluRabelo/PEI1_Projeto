#Recebe as respostas do formulário, valida elas, cria e mostra o currículo 
from django.shortcuts import render, redirect
from .forms import CurriculoForm

def criar_curriculo(request):
    #Se houver requisição, algo enviado no formulário, valida as informaçãoes
    if request.method == "POST":
        form = CurriculoForm(request.POST)
        if form.is_valid():
            request.session['dados'] = form.cleaned_data
            return redirect('escolher_template')
    else:
        form = CurriculoForm()
    return render(request, 'curriculos/form.html', {'form': form})

def escolher_template(request):
    return render(request, 'curriculos/escolher.html')

def visualizar_curriculo(request, modelo_id):
    dados = request.session.get('dados', {})
    template = f'curriculos/modelos/modelo{modelo_id}/index.html'
    return render(request, template, dados)
