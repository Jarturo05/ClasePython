from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


# Crear la aplicacion FastAPI
# Los parametros son metadata para la documentacion automatica
app = FastAPI(
    title="Tienda Dev Senior",
    description="API Backend profesional - Dev Senior Code",
    version="1.0.0"
)

class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    stock: int
    categoria: str

productos_db = [
    {"id": 1, "nombre": "Laptop Dell", "precio": 1299.99, "stock": 15, "categoria": "tecnologia"},
    {"id": 2, "nombre": "Mouse", "precio": 25.0, "stock": 100, "categoria": "tecnologia"},
    {"id": 3, "nombre": "Cuaderno", "precio": 5.5, "stock": 200, "categoria": "papeleria"},
    {"id": 4, "nombre": "Teclado Mecánico", "precio": 150.0, "stock": 40, "categoria": "tecnologia"},
    {"id": 5, "nombre": "Monitor LG 24 pulgadas", "precio": 850.0, "stock": 12, "categoria": "tecnologia"},
    {"id": 6, "nombre": "Impresora Epson", "precio": 620.5, "stock": 8, "categoria": "tecnologia"},
    {"id": 7, "nombre": "Silla de Oficina", "precio": 420.0, "stock": 18, "categoria": "muebles"},
    {"id": 8, "nombre": "Escritorio", "precio": 780.0, "stock": 10, "categoria": "muebles"},
    {"id": 9, "nombre": "Lápiz", "precio": 1.5, "stock": 500, "categoria": "papeleria"},
    {"id": 10, "nombre": "Borrador", "precio": 2.0, "stock": 250, "categoria": "papeleria"}
]
contador_id = 1

"""@app.get("/saludo")
def obtener_saludo():
    return{
        "mensaje": "¡Hola desde FastAPI!",
        "estado": "activo"
    }"""

@app.get("/")
def raiz():
    return {
        "mensaje": "Bienvenido a Tienda Dev Senior",
        "version": "1.0.0"
    }

"""@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "aplicacion": "Tienda Dev Senior"
    }"""

@app.post("/productos")
def crear_producto(producto: ProductoCreate):
    global contador_id
    nuevo = {
        "id": contador_id,
        "nombre": producto.nombre,
        "precio": producto.precio,
        "stock": producto.stock,
        "categoria": producto.categoria
    }
    productos_db.append(nuevo)
    contador_id += 1
    return {"mensaje": "Producto creado exitosamente", "producto": nuevo}

"""@app.get("/productos")
def listar_productos():
    return {
        "total": len(productos_db),
        "productos": productos_db   
    }"""

@app.get("/productos")
def listar_productos(categoria: str | None = None, precio_max: float | None = None):
    resultado = productos_db
    if categoria is not None:
        resultado = [p for p in resultado if p["categoria"].lower() == categoria.lower()]
    if precio_max is not None:
        resultado = [p for p in resultado if p["precio"] <= precio_max]
    return {"total": len(resultado), "productos": resultado}

#La razon por la que va en llaves es que es una variable
@app.get("/productos/{producto_id}")
def obtener_producto_por_iD(producto_id: int):
    for p in productos_db:
        if p["id"] == producto_id:
            return p
    raise HTTPException(status_code=404, detail="Producto no encontrado")

@app.put("/productos/{producto_id}")
def actualizar_producto(producto_id: int, datos: ProductoCreate):
    for p in productos_db:
        if p["id"] == producto_id:
            p["nombre"] = datos.nombre
            p["precio"] = datos.precio
            p["stock"] = datos.stock
            p["categoria"] = datos.categoria
            return {"mensaje": "Producto actualizado", "producto": p}
    raise HTTPException(status_code=404, detail="Producto no encontrado")

@app.delete("/productos/{producto_id}")
def eliminar_producto(producto_id: int):
    for p in productos_db:
        if p["id"] == producto_id:
            productos_db.remove(p)
            return {"mensaje": f"Producto {producto_id} eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Producto no encontrado")