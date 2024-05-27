document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("form-nuevoDiseno");
  
    form.addEventListener("submit", function(event) {
      event.preventDefault();
  
      // Aquí puedes agregar la lógica para enviar los datos del formulario
      // a través de AJAX o realizar otras acciones necesarias.
  
      // Por ejemplo, podrías recopilar los datos del formulario así:
      const nombre = document.getElementById("nombre").value;
      const tipoFilamento = document.getElementById("tipoFilamento").value;
      const genero = document.getElementById("genero").value;
      const descripcion = document.getElementById("descripcion").value;
  
      // Luego, podrías enviar estos datos a través de AJAX
      // usando fetch() o XMLHttpRequest.
  
      // Por ahora, solo mostraremos los datos en la consola.
      console.log("Nombre:", nombre);
      console.log("Tipo de filamento:", tipoFilamento);
      console.log("Colores:", genero);
      console.log("Descripción:", descripcion);
  
      // Si deseas redirigir a otra página después de enviar el formulario,
      // puedes hacerlo usando window.location.href = "url";
  
      // También puedes mostrar un mensaje de éxito o cualquier otra acción que desees.
      alert("¡Formulario enviado con éxito!");
  
      // Aquí puedes reiniciar el formulario si deseas borrar los campos después de enviarlos.
      // form.reset();
    });
  });
  