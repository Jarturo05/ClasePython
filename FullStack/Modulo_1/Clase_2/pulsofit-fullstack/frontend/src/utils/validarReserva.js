const PATRON_CORREO = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

export function validarReserva({ nombre, correo }) {
  const errores = {};
  if (nombre.trim().length < 3) {
    errores.nombre = "Escribe tu nombre (mínimo 3 letras).";
  }
  if (!PATRON_CORREO.test(correo.trim())) {
    errores.correo = "Escribe un correo válido, por ejemplo ana@correo.com.";
  }
  return errores;
}