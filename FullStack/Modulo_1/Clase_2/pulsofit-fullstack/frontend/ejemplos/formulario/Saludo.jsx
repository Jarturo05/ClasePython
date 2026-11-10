import { useState } from "react";
import { createRoot } from "react-dom/client";

function Saludo() {
  const [nombre, setNombre] = useState("");
  const [mensaje, setMensaje] = useState("");

  function enviar(evento) {
    evento.preventDefault();
    if (nombre.trim().length < 3) {
      setMensaje("Escribe al menos 3 letras.");
      return;
    }
    setMensaje(`Hola, ${nombre.trim()}`);
    setNombre("");
  }

  return (
    <form onSubmit={enviar}>
      <input value={nombre} onChange={(evento) => setNombre(evento.target.value)} />
      <button type="submit">Saludar</button>
      <p>{mensaje}</p>
    </form>
  );
}

createRoot(document.getElementById("raiz")).render(<Saludo />);