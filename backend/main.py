from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

#permite que backend y front end se comuniquen.
app.add_middleware(
    CORSMiddleware, #capamidel ware
    allow_origins=["http://localhost:5173"], #especifica la url origen
    allow_credentials=True, #permite credenciales cookies sesion
    allow_methods=["*"], #permite todos los metodos
    allow_headers=["*"], #permite todas las cabeceras
)
@app.get("/")
def inicio():
    return {"mensaje": "IA Job Hunter API funcionando"}
@app.get("/{numero}")
def holamundo(numero : int):
    return {"mensaje" : f"{numero}"}