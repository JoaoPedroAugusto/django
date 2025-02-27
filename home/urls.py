from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
     path('ver_home/', views.ver_home, name='ver_home'),
     
     path("dashboard/", views.dashboard_view, name="dashboard"),  # Página do dashboard
     
     path("colaborador/obter/<int:colaborador_id>/", views.obter_colaborador, name="obter_colaborador"),
     
     path('login/', views.login_view, name='login'),
     
     path("logout/", auth_views.LogoutView.as_view(), name="logout"),
     
     path('cadastro/', views.cadastro_view, name='cadastro'),  
     
     path("colaborador/deletar/<int:colaborador_id>/", views.deletar_colaborador, name="deletar_colaborador"),  
     
       path('colaboradores/', views.listar_colaboradores, name='listar_colaboradores'),
    path('colaboradores/<int:id>/', views.detalhes_colaborador, name='detalhes_colaborador'),
    path('colaboradores/<int:id>/editar/', views.editar_colaborador, name='editar_colaborador'),
    path('colaboradores/<int:id>/deletar/', views.deletar_colaborador, name='deletar_colaborado'),
]
