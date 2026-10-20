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
contador_id = 11


def crear_producto(datos):
    global contador_id
    nuevo = {
        "id": contador_id,
        "nombre":  datos.nombre,
        "precio": datos.precio,
        "stock": datos.stock,
        "categoria": datos.categoria
    }
    productos_db.append(nuevo)
    contador_id += 1
    return nuevo


def listar_productos(categoria= None, precio_max= None):
    resultado = productos_db
    if categoria is not None:
        resultado = [p for p in resultado if p["categoria"].lower() == categoria.lower()]
    if precio_max is not None:
        resultado = [p for p in resultado if p["precio"] <= precio_max]
    return resultado


def obtener_producto (producto_id):
    for p in productos_db:
        if p["id"] == producto_id:
            return p
    return None


def actualizar_producto(producto_id, datos):
    for p in productos_db:
        if p["id"] == producto_id:
            p["nombre"] = datos.nombre
            p["precio"] = datos.precio
            p["stock"] = datos.stock
            p["categoria"] = datos.categoria
            return p
    raise None


def eliminar_producto(producto_id):
    for p in productos_db:
        if p["id"] == producto_id:
            productos_db.remove(p)
            return True
    raise False

def actualizar_parcial_producto(producto_id, datos):
    for p in productos_db:
        if p["id"] == producto_id:
            cambios = datos.model_dump(exclude_unset=True) 
            for campo, valor in cambios.items():
                p[campo] = valor
            return p
    return None