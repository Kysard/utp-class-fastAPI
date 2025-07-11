from fastapi import FastAPI
from app.api import hola, chau

app = FastAPI()

app.include_router(hola.router, prefix="/api", tags=["Saludo"])
app.include_router(chau.router, prefix="/api", tags=["Despedida"])

# Comando para ejecutar el servidor:
# uvicorn app.main:app --reload --port 8001

# Comando para ver la documentación interactiva:
# http://127.0.0.1:8001/docs
