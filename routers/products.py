from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/products",
                  tags=["products"],
                  responses={404: {"message":"no encontrado"}})

products_list= ["producto2","producto2","producto3","producto4"]

@router.get("/")
async def products():
    return products_list

@router.get("/{id}")
async def products(id:int):
    return products_list[id] 

