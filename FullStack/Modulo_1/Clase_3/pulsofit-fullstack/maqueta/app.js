import { clases } from "./datos.js";

const lista = document.querySelector("#lista-clases");
const contador = document.querySelector("#contador");
let misReservas = 0;

function renderizar() {
  lista.innerHTML = clases
    .map(
      (clase) => `
        <article class="tarjeta">
          <h3>${clase.nombre}</h3>
          <p>Entrena: ${clase.entrenador}</p>
          <p>Hora: ${clase.hora}</p>
          <p>Cupos: ${clase.cupos}</p>
          <button class="btn-reservar" data-id="${clase.id}" ${clase.cupos === 0 ? "disabled" : ""}>
            ${clase.cupos === 0 ? "Agotada" : "Reservar"}
          </button>
        </article>
      `
    )
    .join("");

  contador.textContent = misReservas;

  document.querySelectorAll(".btn-reservar").forEach((boton) => {
    boton.addEventListener("click", () => reservar(Number(boton.dataset.id)));
  });
}

function reservar(id) {
  const clase = clases.find((c) => c.id === id);
  if (clase.cupos === 0) return;
  clase.cupos -= 1;
  misReservas += 1;
  renderizar();
}

renderizar();
