from infraestructura.conexion import obtener_conexion

print("Programa iniciado")

with obtener_conexion() as conn:

    conn.execute(
        "INSERT INTO persona (rut, nombre) VALUES (?, ?)",
        ("12345678-9", "Ana Rojas")
    )

    print("Registro insertado")

with obtener_conexion() as conn:

    filas = conn.execute(
        "SELECT rut, nombre FROM persona"
    ).fetchall()

    print("Filas encontradas:")

    for fila in filas:
        print(fila)

print("Programa finalizado")