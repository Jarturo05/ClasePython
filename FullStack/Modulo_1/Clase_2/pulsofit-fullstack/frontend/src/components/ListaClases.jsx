import TarjetaClase from "./TarjetaClase.jsx";

function ListaClases({ clases, onReservar }) {
  return (
    <section className="flex flex-wrap gap-4">
      {clases.map((clase) => (
        <TarjetaClase key={clase.id} clase={clase} onReservar={onReservar} />
      ))}
    </section>
  );
}

export default ListaClases;