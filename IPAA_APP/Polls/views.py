from django.http.response import Http404
from django.shortcuts import render, get_object_or_404

from Polls.models import Pergunta, Resposta, Usuario
from django.template import loader
from django.views import generic


# Create your views here.


def index(request):
    question_list = Pergunta.objects.order_by('sequencia')
    context = {'question_list': question_list}
    return render(request, 'index.html')


def polls(request):
    question_list = Pergunta.objects.order_by('sequencia')
    context = {'question_list': question_list}
    return render(request, 'polls.html', context)


class UsuarioListView(generic.ListView):
    model = Usuario


class PerguntaListView(generic.ListView):
    model = Pergunta
    context_object_name = 'Perguntas'
    queryset = Pergunta.objects.filter()[:1]
    template_name = 'books/my_arbitrary_template_name_list.html'


def detail(request, question_id):
    question = get_object_or_404(Pergunta, pk=question_id)
    return render(request, 'detail.html', {'Pergunta': question})
