import { useEffect, useState } from "react";
import { createRoot } from "react-dom/client";
import axios from "axios";

function Frutas() {
  const [frutas, setFrutas] = useState([]);

  useEffect(() => {
    async function cargar() {
      const respuesta = await axios.get("/ejemplos/api/frutas.json");
      setFrutas(respuesta.data);
    }
    cargar();
  }, []);

  return (
    <ul>
      {frutas.map((fruta) => (
        <li key={fruta.id}>
          {fruta.nombre}: ${fruta.precio}
        </li>
      ))}
    </ul>
  );
}

createRoot(document.getElementById("raiz")).render(<Frutas />);