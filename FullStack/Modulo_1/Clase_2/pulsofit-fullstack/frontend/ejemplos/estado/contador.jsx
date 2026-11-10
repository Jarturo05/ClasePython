import { useState } from "react";
import { createRoot } from "react-dom/client";

function Contador() {
  const [vasos, setVasos] = useState(0);

  function tomar() {
    setVasos(vasos + 1);
  }

  return (
    <div>
      <p>Vasos de agua hoy: {vasos}</p>
      <button onClick={tomar}>Tomé un vaso</button>
    </div>
  );
}

createRoot(document.getElementById("raiz")).render(<Contador />);