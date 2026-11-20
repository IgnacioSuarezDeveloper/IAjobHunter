from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import listar_usuarios
from database import obtener_usuario_por_email
from database import crear_usuario
from pydantic import BaseModel
import hashlib
import secrets


app = FastAPI()
def generar_password_hash(password: str):

    salt = secrets.token_bytes(16)

    hash_bytes = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        600000
    )

    return f"pbkdf2_sha256$600000${salt.hex()}${hash_bytes.hex()}"

class UsuarioCrear(BaseModel):
    nombre: str
    email: str
    password: str

#permite que backend y front end se comuniquen.
app.add_middleware(
    CORSMiddleware, #capamidel ware
    allow_origins=["http://localhost:5173"], #especifica la url origen
    allow_credentials=True, #permite credenciales cookies sesion
    allow_methods=["*"], #permite todos los metodos
    allow_headers=["*"], #permite todas las cabeceras
)
@app.get("/usuarios")
def getUsuarios():
    usuarios = listar_usuarios()
  
    return usuarios

@app.get("/usuarios/email/{email}")
def obtener_usuario_email(email : str):
    usuario = obtener_usuario_por_email(email)
    return usuario

@app.post("/usuarios/nuevoUsuario/")
def crear_usuario_endpoint( usuario : UsuarioCrear):
    password_encriptada = generar_password_hash(usuario.password)
    crear_usuario(usuario.nombre,usuario.email,password_encriptada)
    return "usuario creado"