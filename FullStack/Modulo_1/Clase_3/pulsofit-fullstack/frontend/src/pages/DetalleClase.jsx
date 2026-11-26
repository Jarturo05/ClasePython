import { useEffect, useState } from "react";
import { Link, useNavigate, useParams } from "react-router";
import FormularioReserva from "../components/FormularioReserva.jsx";
import { obtenerClase } from "../services/clasesService.js";
import { crearReserva } from "../services/reservasService.js";

function DetalleClase() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [clase, setClase] = useState(null);
  const [error, setError] = useState("");
  const [errorReserva, setErrorReserva] = useState("");

  useEffect(() => {
    async function cargar() {
      try {
        const datos = await obtenerClase(id);
        setClase(datos);
      } catch (falla) {
        if (falla.response?.status === 404) {
          setError("Esa clase no existe.");
        } else {
          setError("No pudimos cargar la clase. Revisa tu conexión e intenta de nuevo.");
        }
      }
    }
    cargar();
  }, [id]);

  async function confirmar(datos) {
    try {
      await crearReserva({ clase_id: clase.id, ...datos });
      navigate("/mis-reservas");
    } catch (falla) {
      if (falla.response?.status === 409) {
        setErrorReserva("Alguien tomó el último cupo antes que tú. Elige otra clase.");
      } else {
        setErrorReserva("No pudimos guardar tu reserva. Intenta de nuevo en un momento.");
      }
    }
  }

  if (error) {
    return <p className="font-bold text-red-600">{error}</p>;
  }

  if (clase === null) {
    return <p className="text-slate-600">Cargando clase…</p>;
  }

  return (
    <section className="max-w-xl">
      <Link to="/clases" className="text-sm font-bold text-orange-700 underline">
        ← Todas las clases
      </Link>
      <h2 className="mt-3 text-2xl font-bold">{clase.nombre}</h2>
      <p>Entrena: {clase.entrenador}</p>
      <p>Hora: {clase.hora}</p>
      <p className="mb-6">Cupos: {clase.cupos}</p>
      {errorReserva ? (
        <p className="font-bold text-red-600">{errorReserva}</p>
      ) : (
        <FormularioReserva clase={clase} onConfirmar={confirmar} />
      )}
    </section>
  );
}

export default DetalleClase;