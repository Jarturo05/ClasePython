import { createRoot } from "react-dom/client";
import { BrowserRouter, Link, Route, Routes, useParams } from "react-router";

function Libro() {
  const { id } = useParams();
  return <p>Estás leyendo el libro {id}. <Link to="/">Volver</Link></p>;
}

function Portada() {
  return (
    <nav>
      <Link to="/libros/1">Libro 1</Link> · <Link to="/libros/2">Libro 2</Link>
    </nav>
  );
}

createRoot(document.getElementById("raiz")).render(
  <BrowserRouter basename="/ejemplos/rutas">
    <Routes>
      <Route path="/" element={<Portada />} />
      <Route path="/libros/:id" element={<Libro />} />
    </Routes>
  </BrowserRouter>,
);