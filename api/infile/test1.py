from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def create():
    return{"message":"hello"}
    
    