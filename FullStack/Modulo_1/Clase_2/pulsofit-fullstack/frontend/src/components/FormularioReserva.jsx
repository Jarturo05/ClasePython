import { useState } from "react";
import { validarReserva } from "../utils/validarReserva.js";

function FormularioReserva({ clase, onConfirmar }) {
  const [nombre, setNombre] = useState("");
  const [correo, setCorreo] = useState("");
  const [errores, setErrores] = useState({});
  const [mensaje, setMensaje] = useState("");

  function enviar(evento) {
    evento.preventDefault();
    const encontrados = validarReserva({ nombre, correo });
    setErrores(encontrados);
    if (Object.keys(encontrados).length > 0) {
      return;
    }
    onConfirmar({ nombre: nombre.trim(), correo: correo.trim() });
    setMensaje(`¡Listo, ${nombre.trim()}! Tu cupo en ${clase.nombre} quedó reservado.`);
    setNombre("");
    setCorreo("");
  }

  return (
    <form onSubmit={enviar} noValidate className="rounded-lg border border-slate-200 bg-white p-4">
      <h2 className="mb-2 text-xl font-bold">Reserva tu cupo</h2>
      {mensaje && <p className="mb-2 font-bold text-green-700">{mensaje}</p>}
      <p className="mb-4 text-slate-800 font-bold">
        {clase ? `${clase.nombre} · ${clase.hora}` : "Elige una clase con el botón Reservar."}
      </p>

      <label htmlFor="nombre" className="mb-1 block font-bold">
        Nombre
      </label>
      <input
        id="nombre"
        value={nombre}
        onChange={(evento) => setNombre(evento.target.value)}
        className="w-full rounded-md border border-slate-300 px-3 py-2"
      />
      {errores.nombre && <p className="mt-1 text-sm text-red-600">{errores.nombre}</p>}

      <label htmlFor="correo" className="mt-4 mb-1 block font-bold">
        Correo
      </label>
      <input
        id="correo"
        type="email"
        value={correo}
        onChange={(evento) => setCorreo(evento.target.value)}
        className="w-full rounded-md border border-slate-300 px-3 py-2"
      />
      {errores.correo && <p className="mt-1 text-sm text-red-600">{errores.correo}</p>}

      <button
        type="submit"
        disabled={!clase}
        className="mt-4 w-full cursor-pointer rounded-md bg-orange-600 py-2 font-bold text-white hover:bg-orange-700 disabled:cursor-not-allowed disabled:bg-slate-400"
      >
        Confirmar reserva
      </button>
    </form>
  );
}

export default FormularioReserva;