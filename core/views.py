from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def cadastro(request):
    return render(request,'cadastro.html')

def catalago(request):
    return render(request, 'catalago.html')

def contato(request):
    return render(request, 'contato.html')

