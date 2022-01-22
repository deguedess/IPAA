from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usuario/create', views.UserCreate.as_view(), name='usuario_form'),
    path('polls', views.polls, name='polls'),
    path('usuario/', views.index, name='index'),
    path('usuario/', views.UsuarioListView.as_view(), name='usuario'),
    path('pergunta/', views.PerguntaListView.as_view(), name='pergunta'),
    path('<int:question_id>/', views.detail, name='detail'),
]
