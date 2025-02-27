from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm   
from .models import Colaborador, MyFile
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import ColaboradorForm
from django.contrib import messages

def index(request):
    return render(request, "index.html")

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Colaborador, MyFile

def ver_home(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        idade = request.POST.get('idade')
        cpf = request.POST.get('cpf')
        texto = request.POST.get('texto')
        file = request.FILES.get('arquivo')

       
        if file and file.size > 20 * 1024 * 1024:  # 20MB
            messages.error(request, "O arquivo é muito grande! O tamanho máximo permitido é 20MB.")
            return render(request, 'home.html')

       
        colaborador = Colaborador(nome=nome, email=email, telefone=telefone, idade=idade, cpf=cpf, texto=texto)
        colaborador.save()

       
        if file:
            mf = MyFile(tittle='minha_imagem', file=file) 
            mf.save()

        messages.success(request, "Dados e arquivo enviados com sucesso!")
        return redirect('home')  

    return render(request, 'home.html')

@login_required
def dashboard_view(request):
    # Defina o nome de usuário permitido
    usuario_autorizado = 'BomFuturo'  # Nome de usuário específico que pode acessar
    
    # Verifique se o usuário logado é o autorizado
    if request.user.username != usuario_autorizado:
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('home')  # Redireciona para a página inicial ou outra página de sua escolha

    # Se o usuário for autorizado, renderiza o dashboard
    colaboradores = Colaborador.objects.all()  # Exemplo de query para pegar todos os colaboradores
    arquivos = MyFile.objects.all()  # Exemplo de query para pegar todos os arquivos
    return render(request, 'dashboard.html', {'colaboradores': colaboradores, 'arquivos': arquivos})


def obter_colaborador(request, colaborador_id):
    colaborador = get_object_or_404(Colaborador, id=colaborador_id)
    dados = {
        'nome': colaborador.nome,
        'email': colaborador.email,
        'telefone': colaborador.telefone,
        'idade': colaborador.idade,
    }
    return JsonResponse(dados)

# View para deletar um colaborador
def deletar_colaborador(request, colaborador_id):
    colaborador = get_object_or_404(Colaborador, id=colaborador_id)

    if request.method == 'POST':
        colaborador.delete()  # Deleta o colaborador
        return redirect('dashboard')  # Redireciona para o dashboard após a exclusão

    # Se o método não for POST, então apenas renderiza a confirmação de deleção
    return render(request, 'deletar_colaborador.html', {'colaborador': colaborador})

def cadastro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso! Você pode agora fazer login.')
            return redirect('login')  # Redireciona após o cadastro bem-sucedido
        else:
            messages.error(request, 'Erro ao criar a conta. Tente novamente.')
    else:
        form = UserCreationForm()

    return render(request, 'cadastro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login bem-sucedido!')
            return redirect('dashboard')  # Redireciona para a página do dashboard após o login
        else:
            messages.error(request, 'Credenciais inválidas. Tente novamente.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def index(request):
    # Verifica se o usuário está autenticado e se o nome é "BomFuturo"
    exibir_botao_dashboard = False
    if request.user.is_authenticated and request.user.username == "BomFuturo":
        exibir_botao_dashboard = True
    
    return render(request, 'index.html', {'exibir_botao_dashboard': exibir_botao_dashboard})

def editar_colaborador(request, colaborador_id):
    colaborador = get_object_or_404(Colaborador, id=colaborador_id)

    if request.method == 'POST':
        form = ColaboradorForm(request.POST, instance=colaborador)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redireciona para a página de dashboard após salvar

    else:
        form = ColaboradorForm(instance=colaborador)

    return render(request, 'editar_colaborador.html', {'form': form, 'colaborador': colaborador})


def listar_colaboradores(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'dashboard.html', {'colaboradores': colaboradores})

