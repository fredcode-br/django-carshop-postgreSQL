from core.models import Fabricante, Categoria, Veiculo, Tipo , VeiculoImage
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import F
import datetime

def listarImagens(veiculos):
    listaImagens = []
    for veiculo in veiculos:
        fotos = VeiculoImage.objects.filter(veiculo_id=veiculo.id)
        i = 0
        for foto in fotos:
            i= i+1
            if (i == 1):
                veiculo = (veiculo.id, foto.foto)
                listaImagens.append(veiculo)

    return listaImagens

def home(request):
    marca = Fabricante.objects.all().order_by('fabricante')
    categoria = Categoria.objects.all().order_by('categoria')
    menor_ano = Veiculo.objects.all().order_by('ano')[:1]
    maior_ano = Veiculo.objects.all().order_by('-ano')[:1]
    maior_preco = Veiculo.objects.all().order_by('-preco')[:1]
    maior_preco= int(maior_preco[0].preco)

    if request.method == 'POST':
        marca_id = request.POST.get('marca_id')
        modelo_id = request.POST.get('modelo_id')
        Xmenor_preco = request.POST.get('menorPreco')
        Xmaior_preco = request.POST.get('maiorPreco')
        ano = request.POST.get('ano')

        veiculos = Veiculo.objects.filter(status='D').order_by('-vizualizacoes')
        listaImagens = listarImagens(veiculos)

        veiculo_paginator = Paginator(veiculos, 12)
        page_num = request.GET.get('page')
        page = veiculo_paginator.get_page(page_num)

        context = {'page': page, 
                'imagens': listaImagens, 
                'marca': marca, 
                'categoria': categoria,
                'maior_preco': maior_preco,
                'menor_ano': menor_ano,
                'maior_ano': maior_ano}

        return render(request, 'core/estoque.html', context) 
       
    if request.method == 'GET':
        veiculos = Veiculo.objects.filter().order_by('-vizualizacoes')[:8]
        listaImagens = listarImagens(veiculos)
        
        menor_ano = menor_ano[0].ano
        date = datetime.date.today()
        year = int(date.strftime("%Y"))
        anos = []
        for y in range(year-menor_ano+1):
            y = menor_ano+y
            anos.append(y)
            
        context = {
            'marca': marca,
            'categoria': categoria,
            'anos': anos,
            'veiculos': veiculos,
            'imagens': listaImagens,
            'maiorpreco': maior_preco,
        }
        return render(request, 'core/index.html', context)

def estoque(request):
    marca = Fabricante.objects.all().order_by('fabricante')
    categoria = Categoria.objects.all().order_by('categoria')
    menor_ano = Veiculo.objects.all().order_by('ano')[:1]
    maior_ano = Veiculo.objects.all().order_by('-ano')[:1]
    menor_preco = Veiculo.objects.all().order_by('preco')[:1]
    maior_preco = Veiculo.objects.all().order_by('-preco')[:1]
    
    if request.method == "POST":
        novo = request.POST.get('novo')
        seminovo = request.POST.get('seminovo')
        usado = request.POST.get('usado')
        menorPreco = request.POST.get('menorPreco')
        maiorPreco = request.POST.get('maiorPreco')
        menorAno = request.POST.get('menorAno')
        maiorAno = request.POST.get('maiorAno')
        id_marca = request.POST.get('id_marca')
        id_categoria = request.POST.get('id_categoria')

        veiculos = Veiculo.objects.all().order_by('vizualizacoes')
        listaImagens = listarImagens(veiculos)

        veiculo_paginator = Paginator(veiculos, 12)
        page_num = request.GET.get('page')
        page = veiculo_paginator.get_page(page_num)
        
        context = {'page': page, 
                'imagens': listaImagens, 
                'marca': marca, 
                'categoria': categoria,
                'menor_preco': menor_preco,
                'maior_preco': maior_preco,
                'menor_ano': menor_ano,
                'maior_ano': maior_ano}
        
        return render(request, 'core/estoque.html', context)
    
    if request.method == 'GET':
        veiculos = Veiculo.objects.filter(status='D').order_by('-vizualizacoes')
        listaImagens = []
        for veiculo in veiculos:
            fotos = VeiculoImage.objects.filter(veiculo_id=veiculo.id)
            i = 0
            for foto in fotos:
                i= i+1
                if (i == 1):
                    veiculo = (veiculo.id, foto.foto)
                    listaImagens.append(veiculo)

        veiculo_paginator = Paginator(veiculos, 12)
        page_num = request.GET.get('page')
        page = veiculo_paginator.get_page(page_num)

        context = {'page': page, 
                'imagens': listaImagens, 
                'marca': marca, 
                'categoria': categoria,
                'menor_preco': menor_preco,
                'maior_preco': maior_preco,
                'menor_ano': menor_ano,
                'maior_ano': maior_ano}
        
        return render(request, 'core/estoque.html', context)

def anuncio(request, id):
    imagens = VeiculoImage.objects.filter(veiculo_id=id)
    Veiculo.objects.filter(id=id).update(vizualizacoes=F('vizualizacoes')+1)

    if request.method == 'GET':
        veiculo = Veiculo.objects.get(id=id)
        context = {'veiculo': veiculo, 'imagens': imagens}
        return render(request, 'core/anuncio.html', context)