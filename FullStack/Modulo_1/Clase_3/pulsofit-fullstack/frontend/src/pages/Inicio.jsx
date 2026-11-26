import { Link } from "react-router";

function Inicio() {
  return (
    <section className="mx-auto max-w-xl py-10 text-center">
      <h2 className="mb-3 text-3xl font-bold">Entrena a tu ritmo</h2>
      <p className="mb-6 text-slate-600">
        Mira las clases de hoy y reserva tu cupo antes de que se agote.
      </p>
      <Link
        to="/clases"
        className="rounded-md bg-orange-600 px-5 py-3 font-bold text-white hover:bg-orange-700"
      >
        Ver las clases
      </Link>
    </section>
  );
}

export default Inicio;