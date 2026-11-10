import { useState } from "react";
import { createRoot } from "react-dom/client";

function Bombillo({ encendida }) {
  return <p>{encendida ? "Luz encendida" : "Luz apagada"}</p>;
}

function Interruptor({ encendida, onCambiar }) {
  return <button onClick={onCambiar}>{encendida ? "Apagar" : "Encender"}</button>;
}

function Habitacion() {
  const [encendida, setEncendida] = useState(false);

  return (
    <div>
      <Bombillo encendida={encendida} />
      <Interruptor encendida={encendida} onCambiar={() => setEncendida(!encendida)} />
    </div>
  );
}

createRoot(document.getElementById("raiz")).render(<Habitacion />);