import { useState } from "react";
import Encabezado from "./components/Encabezado.jsx";
import PiePagina from "./components/PiePagina.jsx";
import ListaClases from "./components/ListaClases.jsx";
import FormularioReserva from "./components/FormularioReserva.jsx";
import MisReservas from "./components/MisReservas.jsx";
import { clases } from "./data/clases.js";

function App() {
  const [listaClases, setListaClases] = useState(clases);
  const [idElegida, setIdElegida] = useState(null);
  const [reservas, setReservas] = useState([]);

  const claseElegida = listaClases.find((clase) => clase.id === idElegida);

  function confirmarReserva(datos) {
    setListaClases(
      listaClases.map((clase) =>
        clase.id === idElegida ? { ...clase, cupos: clase.cupos - 1 } : clase,
      ),
    );
    setReservas([
      ...reservas,
      { id: reservas.length + 1, clase: claseElegida.nombre, hora: claseElegida.hora, ...datos },
    ]);
    setIdElegida(null);
  }

  return (
    <div className="min-h-screen bg-slate-100 text-slate-900">
      <Encabezado />
      <main className="grid gap-6 p-6 lg:grid-cols-[1fr_320px]">
        <div>
          <h2 className="mb-4 text-xl font-bold">Clases de hoy</h2>
          <ListaClases clases={listaClases} onReservar={setIdElegida} />
        </div>
        <aside className="flex flex-col gap-6">
          <FormularioReserva clase={claseElegida} onConfirmar={confirmarReserva} />
          <MisReservas reservas={reservas} />
        </aside>
      </main>
      <PiePagina />
    </div>
  );
}

export default App;