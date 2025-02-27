
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("file-input").addEventListener("change", function() {
        let file = this.files[0];
        let maxSize = 20 * 1024 * 1024;  // 20MB

        if (file && file.size > maxSize) {
            alert("O arquivo é muito grande! O tamanho máximo permitido é 20MB.");
            this.value = "";  // Apaga o campo de upload
        }
    });
});



document.getElementById("menu-toggle").addEventListener("click", function () {
    let menu = document.getElementById("menu");
    menu.classList.toggle("hidden");
});

