import { useEffect, useState } from "react";
import ListaClases from "../components/ListaClases.jsx";
import { listarClases } from "../services/clasesService.js";

function Clases() {
  const [clases, setClases] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    async function cargar() {
      try {
        const datos = await listarClases();
        setClases(datos);
      } catch {
        setError("No pudimos cargar las clases. Revisa tu conexión e intenta de nuevo.");
      }
    }
    cargar();
  }, []);

  if (error) {
    return <p className="font-bold text-red-600">{error}</p>;
  }

  if (clases === null) {
    return <p className="text-slate-600">Cargando clases…</p>;
  }

  return (
    <section>
      <h2 className="mb-4 text-xl font-bold">Clases de hoy</h2>
      <ListaClases clases={clases} />
    </section>
  );
}

export default Clases;