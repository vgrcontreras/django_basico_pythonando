from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa

# Create your views here.
def ver_produtos(request):
    if request.method == 'GET':
        nome = 'victor'

        return render(
            request,
            template_name='ver_produto.html',
            context={'nome': nome}
            )
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')

        pessoas = Pessoa.objects.filter(nome=nome)

        if pessoas.exists():
            return HttpResponse('Usuário já cadastrado')
        else:
            pessoa_db = Pessoa(nome=nome,
                            idade=idade
                            )
            
            pessoa_db.save()

            return HttpResponse('Dados cadastrado com sucesso')



def inserir_produtos(request):
    return HttpResponse('inserir produtos')
