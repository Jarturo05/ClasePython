"""
Sistema de Biblioteca

Relaciones:
- Autor es la clase base
- AutorPremium hereda de Autor → herencia
- Biblioteca tiene Libros → agregación
  (un libro puede existir sin biblioteca)
- Libro tiene Capitulos → composición
  (los capítulos no existen sin el libro)

Clases a crear:

Autor
    - nombre
    - nacionalidad
    - presentarse()

AutorPremium hereda de Autor
    - reconocimiento (ej: "Premio Nobel")
    - mostrar_reconocimiento()

Capitulo           ← composición
    - titulo
    - paginas
    - mostrar_info()

Libro              ← crea sus Capitulos adentro
    - titulo
    - autor (objeto Autor) ← agregación
    - capitulos = []
    - agregar_capitulo(titulo, paginas)
    - mostrar_info()      ← muestra título, autor y capítulos

Biblioteca         ← recibe Libros desde afuera
    - nombre
    - libros = []
    - agregar_libro(libro)
    - mostrar_catalogo()
"""