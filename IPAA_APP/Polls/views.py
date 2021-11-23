from django.shortcuts import render

from Polls.models import Pergunta, Resposta, Usuario
from django.views import generic


# Create your views here.


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_polls = Pergunta.objects.all().count()
    num_answers = Resposta.objects.all().count()

    # Available books (status = 'a')
    num_polls_active = Pergunta.objects.filter(
        status__exact=True).count()

    context = {
        'num_polls': num_polls,
        'num_answers': num_answers,
        'num_polls_active': num_polls_active,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class UsuarioListView(generic.ListView):
    model = Usuario


class PerguntaListView(generic.ListView):
    model = Pergunta
    context_object_name = 'Perguntas'
    queryset = Pergunta.objects.filter()[:1]
    template_name = 'books/my_arbitrary_template_name_list.html'
