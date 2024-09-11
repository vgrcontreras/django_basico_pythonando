from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ver_produtos(request):
    nome = 'victor'

    return render(
        request,
        template_name='ver_produto.html',
        context={'nome': nome}
        )

def inserir_produtos(request):
    return HttpResponse('inserir produtos')
