from django.shortcuts import render

def cnIndex(request):
    return render(request, 'cn_main.html')