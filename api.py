from fastapi import FastAPI, UploadFile, File, Form, Depends
from typing import Optional
from pydantic import BaseModel
import shutil
import os
import uuid
import orm.repo as repo
from sqlalchemy.orm import Session
from orm.config import generador_sesion

app = FastAPI()


#funcion que devuelve la lista de alumnos 
@app.get("/alumnos")
def all_alumnos(session: Session = Depends(generador_sesion)):
    print("obteniendo todos los alumnos")
    return repo.find_all_alumnos(session)


#funcion que devuelve el alumno correspondiente a un id
@app.get("/alumnos/{id}")
def alumno_byID(id_alumno: int, session: Session = Depends(generador_sesion)):
    print("obteniendo alumno por id de alumno: ", id_alumno)
    return repo.find_alumno_biID(session, id_alumno)


#funcion que devuelve todas las calificaciones de un alumno
@app.get("/alumnos/{id}/calificaciones")
def calificaciones_by_alumnoID(id_alumno:int, session:Session = Depends(generador_sesion)):
    print("obteniendo calificacion por id de alumno: ", id_alumno)
    return repo.find_calificaciones_by_alumnoID(session,id_alumno)

#funcion que devuelve todas las fotos de un alumno
@app.get("/alumnos/{id}/fotos")
def fotos_by_alumnoID(id_alumno:int, session:Session = Depends(generador_sesion)):
    print("obteniendo fotos por id de alumno:", id_alumno)
    return repo.find_fotos_by_alumnoID(session,id_alumno)


#funcion que devuelve la foto correspondiente a un id_foto
@app.get("/fotos/{id}")
def fotos_byID(id_foto:int, session: Session = Depends(generador_sesion)):
    print("obteniendo foto por id: ", id_foto)
    return repo.find_foto_byID(session,id_foto)


#funcion que devuelve la calificacion correspondiente a un id_calificacion
@app.get("/calificaciones/{id}")
def calificacion_byID(id_calificacion:int, session: Session = Depends(generador_sesion)):
    print("obteniendo calificacion por id: ", id_calificacion)
    return repo.find_calificacion_byID(session, id_calificacion)

#borra una foto por id_foto
@app.delete("/fotos/{id}")
def borrar_foto_byID(id_foto:int, session:Session = Depends(generador_sesion)):
    print("borrando foto por id: ", id_foto)
    return repo.del_foto_byID(session, id_foto)

#borra la calificacion por id_calificacion
@app.delete("/calificaciones/{id}")
def borrar_calificaciones_byID(id_calificacion:int, session:Session = Depends(generador_sesion)):
    print("borrando calificacion por id: ", id_calificacion)
    return repo.del_calificacion_byID(session, id_calificacion)


#borra todas las fotos de un alumno por id_alumno
@app.delete("/alumnos/{id}/fotos")
def borrar_foto_by_alumnoID(id_alumno:int, session:Session = Depends(generador_sesion)):
    print("borrando fotos por id de alumno: ", id_alumno)
    return repo.del_fotos_by_alumnoID(session,id_alumno)


#borra todas las calificaciones de un alumno por id_alumno
@app.delete("/alumnos/{id}/calificaciones")
def borrar_calificacion_by_alumnoID(id_alumno:int, session:Session = Depends(generador_sesion)):
    print("borrando calificaciones por id de alumno: ",id_alumno)
    return repo.del_calificaciones_by_alumnoID(session, id_alumno)

#borra un alumno
@app.delete("/alumnos/{id}")
def borrar_alumno_byID(id_alumno:int, session:Session = Depends(generador_sesion)):
    print("borrando alumno por id: ", id_alumno)
    return repo.del_alumnos_byID(session,id_alumno)




