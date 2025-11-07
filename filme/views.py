from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView


# Create your views here.
#n vai ser mais usado, foi so pra praticar
#def homepage(request):
    #return render(request, 'homepage.html')

class Homepage(TemplateView):
    template_name = 'homepage.html'

#def clipezudos(request):
    #contexto = {}
    #lista_filmes = Filme.objects.all()
    #contexto['lista_filmes'] = lista_filmes
    #return render(request, 'clipezudos.html', contexto)

class Clipezudos(ListView):
    template_name  = 'clipezudos.html'
    model = Filme

class DescricaoClipezudo(DetailView):
    template_name = 'descricao_clipezudo.html'
    model = Filme
