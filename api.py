from fastapi import FastAPI, UploadFile, File, Form
from typing import Optional
from pydantic import BaseModel
import shutil
import os #Para acceder a la ruta del home
import uuid #generar un nombre aleatorio

# creación del servidor
app = FastAPI()

#definición de la base del usuario
class UsuarioBase(BaseModel):
    nombre:str
    direccion:str 

@app.post("/usuario")
async def guarda_foto(nombre:str=Form(...), direccion:str=Form(...), foto:UploadFile=File(...), uservip:str|None=Form(None)):   #Form(...)--->operador elipsis
    print("Titulo: ", nombre)
    print("Dirección: ", direccion)
    home_user = os.path.expanduser("~")
    home_usuario = os.path.normpath(home_user)
    nombre_archivo = uuid.uuid4() #nombre en formato
    extension_foto = os.path.splitext(foto.filename)[1]
    is_checked = uservip is not None
    if(is_checked):
        ruta_imagen = f'{home_usuario}/fotos-usuarios-vip/{nombre_archivo}{extension_foto}'
        print("Guardando la foto en:", ruta_imagen)
        with open(ruta_imagen,"wb") as imagen:
            contenido = await foto.read()
            imagen.write(contenido)
    else:
        ruta_imagen = f'{home_usuario}/fotos-usuarios/{nombre_archivo}{extension_foto}'
        print("Guardando la foto en:", ruta_imagen)
        with open(ruta_imagen,"wb") as imagen:
            contenido = await foto.read()
            imagen.write(contenido)
        
    
    respuesta = {
        "Nombre" : nombre,
        "Dirección" : direccion,
        "Ruta" : ruta_imagen
    }
    return respuesta

