
import os
import psycopg
from dotenv import load_dotenv
from pathlib import Path


# Localizar el archivo .env
RUTA_ENV = Path(__file__).resolve().parent / ".env"

# Cargar las variables de entorno
load_dotenv(RUTA_ENV)

# Obtener las credenciales de PostgreSQL
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")


# Función para establecer la conexión con PostgreSQL
def obtener_conexion():

    # Crear la conexión utilizando las credenciales
    conexion = psycopg.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    # Devolver el objeto de conexión
    return conexion

def listar_usuarios():
    usuarios = []
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id,nombre,email FROM usuarios")
            respuesta = cursor.fetchall()
            for fila in respuesta:
                 usuario = {
                    "id" : fila[0],
                    "nombre" : fila[1],
                    "email" : fila[2]
                 }
                 usuarios.append(usuario)
            return usuarios

def obtener_usuario_por_email(email):
    # Este bloque se ejecuta únicamente si abrimos database.py directamente
        
            # Abrir conexión con PostgreSQL
            with obtener_conexion() as conexion:
    
                # Crear cursor para ejecutar consultas SQL
                with conexion.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM usuarios where email = %s", (email,)
                    )
                    respuesta = cursor.fetchone()
                    return respuesta

def crear_usuario(nombre, email, password_hash):
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(
                "INSERT INTO usuarios (nombre, email, password_hash) VALUES (%s, %s, %s)",
                (nombre, email, password_hash)
            )