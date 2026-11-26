import { useEffect, useState } from "react";
import { listarReservas } from "../services/reservasService.js";

function MisReservas() {
  const [reservas, setReservas] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    async function cargar() {
      try {
        const datos = await listarReservas();
        setReservas(datos);
      } catch {
        setError("No pudimos cargar tus reservas. Revisa tu conexión e intenta de nuevo.");
      }
    }
    cargar();
  }, []);

  if (error) {
    return <p className="font-bold text-red-600">{error}</p>;
  }

  if (reservas === null) {
    return <p className="text-slate-600">Cargando reservas…</p>;
  }

  return (
    <section className="rounded-lg border border-slate-200 bg-white p-4">
      <h2 className="mb-2 text-xl font-bold">Mis reservas ({reservas.length})</h2>
      {reservas.length === 0 ? (
        <p className="text-slate-600">Aún no tienes reservas.</p>
      ) : (
        <ul className="list-disc pl-5">
          {reservas.map((reserva) => (
            <li key={reserva.id}>
              {reserva.clase} · {reserva.hora} · {reserva.nombre}
            </li>
          ))}
        </ul>
      )}
    </section>
  );
}

export default MisReservas;