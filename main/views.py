from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title':'main',
        'content': 'Главная страница магазина Home',
        'list':[1,2],
        'dict': {'first':1},
        'istrue':False
    }
    
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('about us')