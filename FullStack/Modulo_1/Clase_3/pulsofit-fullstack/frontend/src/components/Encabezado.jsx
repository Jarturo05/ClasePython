import { Link } from "react-router";

function Encabezado() {
  return (
    <header className="flex items-center justify-between bg-slate-900 px-6 py-4 text-white">
      <h1 className="text-2xl font-bold">PulsoFit</h1>
      <nav className="flex gap-4 text-sm">
        <Link to="/" className="hover:text-orange-300">Inicio</Link>
        <Link to="/clases" className="hover:text-orange-300">Clases</Link>
        <Link to="/mis-reservas" className="hover:text-orange-300">Mis reservas</Link>
      </nav>
    </header>
  );
}

export default Encabezado;