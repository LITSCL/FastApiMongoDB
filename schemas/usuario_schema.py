from typing import List

from models.usuario import Usuario

def schema(usuario: Usuario) -> dict:
    return {
        "id": str(usuario["_id"]),
        "nombre": usuario["nombre"],
        "correo": usuario["correo"],
        "clave": usuario["clave"]
    }

def objeto_schema(usuario: Usuario) -> dict:
    return schema(usuario)
    
def lista_schema(usuarios: List[Usuario]) -> list:
    return [schema(usuario) for usuario in usuarios]