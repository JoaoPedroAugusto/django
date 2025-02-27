function abrirEditar(colaboradorId) {
    fetch(`/home/colaborador/obter/${colaboradorId}/`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("nome").value = data.nome;
            document.getElementById("email").value = data.email;
            document.getElementById("telefone").value = data.telefone;
            document.getElementById("idade").value = data.idade;
            document.getElementById("cpf").value = data.cpf;
            document.getElementById("texto").value = data.texto;

            document.getElementById("modalEditar").style.display = "block";
        });
}

function fecharModal() {
    document.getElementById("modalEditar").style.display = "none";
}

function deletarColaborador(colaboradorId) {
    if (confirm("Você tem certeza que deseja deletar este colaborador?")) {
        window.location.href = `/home/colaborador/deletar/${colaboradorId}/`;
    }
}

 // Script para abrir/fechar o menu mobile
 document.getElementById("menu-toggle").addEventListener("click", function () {
    document.getElementById("menu").classList.toggle("hidden");
});

document.addEventListener("DOMContentLoaded", function () {
    // MENU MOBILE
    const menuToggle = document.getElementById("menu-toggle");
    const menu = document.getElementById("menu");
    
    menuToggle.addEventListener("click", function () {
        menu.classList.toggle("hidden");
    });

    // MODAL DE EDIÇÃO
    const modalEditar = document.getElementById("modalEditar");
    const formEditar = document.getElementById("formEditar");

    window.abrirEditar = function (id) {
        fetch(`/api/colaboradores/${id}/`) // Ajuste a URL conforme necessário
            .then(response => response.json())
            .then(data => {
                document.getElementById("nome").value = data.nome;
                document.getElementById("email").value = data.email;
                document.getElementById("telefone").value = data.telefone;
                document.getElementById("idade").value = data.idade;
                document.getElementById("cpf").value = data.cpf;
                document.getElementById("texto").value = data.texto;
                formEditar.action = `/editar_colaborador/${id}/`; // Ajuste a URL
                modalEditar.style.display = "block";
            })
            .catch(error => console.error("Erro ao buscar dados do colaborador:", error));
    };

    window.fecharModal = function () {
        modalEditar.style.display = "none";
    };

    // FECHAR MODAL AO CLICAR FORA
    window.addEventListener("click", function (event) {
        if (event.target === modalEditar) {
            fecharModal();
        }
    });

    // DELETAR COLABORADOR
    window.deletarColaborador = function (id) {
        if (confirm("Tem certeza que deseja deletar este colaborador?")) {
            fetch(`/deletar_colaborador/${id}/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCSRFToken(),
                    "Content-Type": "application/json"
                },
            })
            .then(response => {
                if (response.ok) {
                    location.reload();
                } else {
                    alert("Erro ao deletar colaborador");
                }
            })
            .catch(error => console.error("Erro ao deletar colaborador:", error));
        }
    };

    // FUNÇÃO PARA PEGAR O CSRF TOKEN DO DJANGO
    function getCSRFToken() {
        return document.querySelector("[name=csrfmiddlewaretoken]").value;
    }
});
