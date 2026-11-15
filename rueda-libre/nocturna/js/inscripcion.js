// Validación nativa y explicación honesta del estado de la demo.
const formulario = document.querySelector("#registro-nocturno");
const estado = document.querySelector("#estado-inscripcion");
if (formulario && estado) {
    formulario.addEventListener("submit", (evento) => {
        evento.preventDefault();
        if (!formulario.reportValidity()) return;
        estado.textContent = "Los datos son válidos. Esta es una demostración: tu solicitud NO ha sido enviada. Para recibir inscripciones reales es necesario conectar un backend o servicio de formularios.";
        estado.classList.add("font-bold", "text-verde-ruta", "dark:text-amarillo-farol");
        estado.focus?.();
    });
}
