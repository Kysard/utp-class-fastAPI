from fastapi import APIRouter

router = APIRouter()

@router.get("/chau")
def decir_chau():
    return {"mensaje": "Chau desde FastAPI"}
