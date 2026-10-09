import os
import sqlite3

from contextlib import contextmanager
from dotenv import load_dotenv

load_dotenv()


@contextmanager
def obtener_conexion():

    ruta = os.environ.get("DB_NOMBRE")

    conn = sqlite3.connect(ruta)

    try:
        yield conn
        conn.commit()

    finally:
        conn.close()
