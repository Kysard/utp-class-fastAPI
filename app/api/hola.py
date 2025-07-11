from fastapi import APIRouter

router = APIRouter()

@router.get("/hola")
def decir_hola():
    return {"mensaje": "Hola desde FastAPI"}
