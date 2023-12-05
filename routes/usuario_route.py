from fastapi import APIRouter
from typing import List
from bson.objectid import ObjectId

from config.database import DataBase
from models.usuario import Usuario
from schemas.usuario_schema import objeto_schema, lista_schema

db: object = DataBase().get_conexion()
router: object = APIRouter()

query: object = None

@router.post("/usuario/save", response_model = str, tags = ["modelo_usuario"])
async def save_usuario(usuario: Usuario) -> str:
    usuario_obtenido: dict = dict(usuario)
    usuario_obtenido.pop("id")
    query = db.usuario.insert_one(usuario_obtenido)
    resultado: str = str(query.inserted_id)
    return resultado

@router.get("/usuario", response_model = List[Usuario], tags = ["modelo_usuario"])
async def get_usuarios() -> list:
    query = db.usuario.find()
    resultado: list = lista_schema(query)
    return resultado

@router.get("/usuario/{key}", response_model = Usuario, tags = ["modelo_usuario"])
async def get_usuario(key: str) -> dict:
    query = db.usuario.find_one({"_id": ObjectId(key)})
    resultado: dict = objeto_schema(query)
    return resultado

@router.put("/usuario/{key}", response_model = Usuario, tags = ["modelo_usuario"])
async def update_usuario(key: str, usuario: Usuario) -> dict:
    query = db.usuario.find_one_and_update({"_id": ObjectId(key)}, {"$set": dict(usuario)})
    resultado: dict = objeto_schema(query)
    return resultado

@router.delete("/usuario/{key}", response_model = Usuario, tags = ["modelo_usuario"])
async def delete_usuario(key: str) -> dict:
    query = db.usuario.find_one_and_delete({"_id": ObjectId(key)})
    resultado: dict = objeto_schema(query)
    return resultado

rutas_usuario: object = router