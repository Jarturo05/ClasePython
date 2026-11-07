import Encabezado from "./components/Encabezado.jsx";
import PiePagina from "./components/PiePagina.jsx";
import ListaClases from "./components/ListaClases.jsx";
import { clases } from "./data/clases.js";

function App() {
  function reservar(id) {
    const clase = clases.find((c) => c.id === id);
    if (clase.cupos === 0) {
      console.log(`${clase.nombre} ya no tiene cupos.`);
      return;
    }
    clase.cupos -= 1;
    console.log(`Reservaste ${clase.nombre}. Quedan ${clase.cupos} cupos.`);
  }

  return (
    <div className="min-h-screen bg-slate-100 text-slate-900">
      <Encabezado />
      <main className="p-6">
        <h2 className="mb-4 text-xl font-bold">Clases de hoy</h2>
        <ListaClases clases={clases} onReservar={reservar} />
      </main>
      <PiePagina />
    </div>
  );
}

export default App;