import axios from "axios";

const URL_API = "http://localhost:8000";

export async function listarClases() {
  const respuesta = await axios.get(`${URL_API}/clases`);
  return respuesta.data;
}

export async function obtenerClase(id) {
  const respuesta = await axios.get(`${URL_API}/clases/${id}`);
  return respuesta.data;
}