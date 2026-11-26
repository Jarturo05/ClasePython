import { Link } from "react-router";

function TarjetaClase({ clase }) {
  return (
    <article className="w-56 rounded-lg border border-slate-200 bg-white p-4 shadow-sm">
      <h3 className="mb-2 text-lg font-bold">{clase.nombre}</h3>
      <p>Entrena: {clase.entrenador}</p>
      <p>Hora: {clase.hora}</p>
      <p>Cupos: {clase.cupos}</p>
      <Link
        to={`/clases/${clase.id}`}
        className="mt-3 block rounded-md bg-orange-600 py-2 text-center font-bold text-white hover:bg-orange-700"
      >
        {clase.cupos === 0 ? "Ver clase (agotada)" : "Ver y reservar"}
      </Link>
    </article>
  );
}

export default TarjetaClase;