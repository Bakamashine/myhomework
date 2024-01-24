from django.shortcuts import render
from .models import Spisok
def index(req):
    bss = Spisok.objects.all();
    return render(req, 'osnova/index.html', {'bss':bss})
def zagl(req):
    return render(req, 'osnova/zaglushka.html')
# Create your views here.
