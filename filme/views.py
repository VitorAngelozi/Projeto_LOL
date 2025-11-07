from django.shortcuts import render
from .models import Filme, Musica
from django.views.generic import TemplateView, ListView, DetailView


# Create your views here.

class Homepage(TemplateView):
    template_name = 'homepage.html'

class Clipezudos(ListView):
    template_name  = 'clipezudos.html'
    model = Filme

class DescricaoClipezudo(DetailView):
    template_name = 'descricao_clipezudo.html'
    model = Musica