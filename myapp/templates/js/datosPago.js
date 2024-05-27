document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("form-agregarCliente");

    form.addEventListener("submit", function(event) {
        event.preventDefault(); // Evitar el envío del formulario por defecto
        validarFormulario();
    });

    function validarFormulario() {
        // Validar campos del formulario
        const nombre = document.getElementById("edit-input-name").value.trim();
        const apellidos = document.getElementById("edit-input-lastname").value.trim();
        const correo = document.getElementById("edit-input-correo").value.trim();
        const telefono = document.getElementById("edit-input-telefono").value.trim();
        const direccion = document.getElementById("edit-input-direccion").value.trim();
        const cp = document.getElementById("edit-input-cp").value.trim();

        if (nombre === "" || apellidos === "" || correo === "" || telefono === "" || direccion === "" || cp === "") {
            alert("Por favor completa todos los campos del formulario.");
            return;
        }

        // Aquí puedes agregar más validaciones según tus necesidades

        // Si el formulario pasa todas las validaciones, puedes enviar los datos
        enviarDatos();
    }

    function enviarDatos() {
        // Obtener los datos del formulario
        const datosFormulario = {
            nombre: document.getElementById("edit-input-name").value.trim(),
            apellidos: document.getElementById("edit-input-lastname").value.trim(),
            correo: document.getElementById("edit-input-correo").value.trim(),
            telefono: document.getElementById("edit-input-telefono").value.trim(),
            direccion: document.getElementById("edit-input-direccion").value.trim(),
            cp: document.getElementById("edit-input-cp").value.trim()
        };

        // Enviar los datos mediante una solicitud AJAX
        const xhr = new XMLHttpRequest();
        xhr.open("POST", "ruta-de-base-datos", true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4 && xhr.status === 200) {
                alert("Datos enviados correctamente.");
            }
        };
        xhr.send(JSON.stringify(datosFormulario));
        // Aquí puedes agregar la lógica para enviar los datos del formulario
        // Por ejemplo, puedes enviar los datos mediante una solicitud AJAX o redireccionar a otra página
        alert("Datos enviados correctamente.");
    }

    // Agregar funcionalidad al botón de enviar
    const btnEnviar = document.querySelector(".btn-enviar");
    btnEnviar.addEventListener("click", function() {
        validarFormulario();
    });
});

