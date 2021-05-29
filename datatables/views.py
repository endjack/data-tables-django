from django.shortcuts import render
from django.views.generic import ListView
from .models import Cliente

# Create your views here.

class ListarClientesView(ListView):
    template_name = "index.html"
    queryset = Cliente.objects.all()
    context_object_name ='list'
