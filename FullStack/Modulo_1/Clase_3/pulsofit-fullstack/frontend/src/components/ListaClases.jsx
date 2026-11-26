import TarjetaClase from "./TarjetaClase.jsx";

function ListaClases({ clases }) {
  return (
    <section className="flex flex-wrap gap-4">
      {clases.map((clase) => (
        <TarjetaClase key={clase.id} clase={clase} />
      ))}
    </section>
  );
}

export default ListaClases;