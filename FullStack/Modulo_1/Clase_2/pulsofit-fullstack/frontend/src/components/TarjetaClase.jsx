function TarjetaClase({ clase, onReservar }) {
  return (
    <article className="w-56 rounded-lg border border-slate-200 bg-white p-4 shadow-sm">
      <h3 className="mb-2 text-lg font-bold">{clase.nombre}</h3>
      <p>Entrena: {clase.entrenador}</p>
      <p>Hora: {clase.hora}</p>
      <p>Cupos: {clase.cupos}</p>
      <button
        type="button"
        disabled={clase.cupos === 0}
        onClick={() => onReservar(clase.id)}
        className="mt-3 w-full cursor-pointer rounded-md bg-orange-600 py-2 font-bold text-white hover:bg-orange-700 disabled:cursor-not-allowed disabled:bg-slate-400"
      >
        {clase.cupos === 0 ? "Agotada" : "Reservar"}
      </button>
    </article>
  );
}

export default TarjetaClase;