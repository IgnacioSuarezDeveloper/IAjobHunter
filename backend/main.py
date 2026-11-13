from fastapi import FastAPI
app = FastAPI()

@app.get("/{numero}")
def holamundo(numero : int):
    return {"mensaje" : f"{numero}"}