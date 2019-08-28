from django.shortcuts import render
from .models import Portfolio

def cnIndex(request):
    Portfolios = Portfolio.objects.all()
    return render(request, 'cn_main.html', {"portfolio":Portfolios})