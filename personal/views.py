from django.shortcuts import render
from cn_vson.models import Bio

def index(request):
    Bios = Bio.objects.all()
    content = {"Bios":Bios}
    return render(request, 'personal/header.html',content)
