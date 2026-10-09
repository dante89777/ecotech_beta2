import sqlite3

conn = sqlite3.connect("ecotech.db")

with open(
    "db/01_esquema.sql",
    encoding="utf-8"
) as archivo:

    conn.executescript(
        archivo.read()
    )

conn.close()

print("Base creada")
