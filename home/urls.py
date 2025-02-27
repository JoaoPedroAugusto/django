from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Página inicial
    path('ver_home/', views.ver_home, name='ver_home'),

    # Dashboard
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # Autenticação
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastro/', views.cadastro_view, name='cadastro'),

    # Colaboradores
    path('colaboradores/', views.listar_colaboradores, name='listar_colaboradores'),
    
    path('colaboradores/<int:colaborador_id>/editar/', views.editar_colaborador, name='editar_colaborador'),
    path('colaboradores/<int:colaborador_id>/deletar/', views.deletar_colaborador, name='deletar_colaborador'),

    # Obter dados de um colaborador (para AJAX, por exemplo)
    path('colaborador/obter/<int:colaborador_id>/', views.obter_colaborador, name='obter_colaborador'),
]