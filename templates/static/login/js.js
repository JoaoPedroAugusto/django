function deletarColaborador(colaboradorId) {
    if (confirm("Você tem certeza que deseja deletar este colaborador?")) {
        // Redireciona para a view de deletar, onde será tratado o POST para deletar
        window.location.href = `/home/colaborador/deletar/${colaboradorId}/`;
    }
}