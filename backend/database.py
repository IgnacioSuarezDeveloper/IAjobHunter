
import os
import psycopg
from dotenv import load_dotenv
from pathlib import Path

# Cargar variables del archivo .env
RUTA_ENV = Path(__file__).resolve().parent / ".env"
load_dotenv(RUTA_ENV)

# Obtener credenciales
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")


# Crear conexión con PostgreSQL
def obtener_conexion():
    conexion = psycopg.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    return conexion


# Prueba de conexión
if __name__ == "__main__":
    with obtener_conexion() as conexion:
        print("¡Conexión con PostgreSQL correcta!")
