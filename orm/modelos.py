from orm.config import BaseClass

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, FLOAT

import datetime

#mapeo de la tabla alumnos
class Alumno(BaseClass):
    __tablename__ = "alumnos"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    edad = Column(Integer)
    domicilio = Column(String(100))
    carrera = Column(String(100))
    trimestre = Column(String(100))
    email = Column(String(100))
    password = Column(String(100))
    fecha_registro = Column(DateTime(timezone=True), default = datetime.datetime.now)

#mapeo de la tabla calificaciones
class Calificacion(BaseClass):
    __tablename__ = "calificaciones"
    id = Column(Integer, primary_key=True)
    id_alumno = Column(Integer, ForeignKey ("alumnos.id"))
    uea = Column(String(100))
    calificacion = Column(String(100))


#mapeo de la tabla fotos
class Foto(BaseClass):
    __tablename__ = "fotos"
    id = Column(Integer, primary_key=True)
    id_alumno = Column(Integer, ForeignKey ("alumnos.id"))
    titulo = Column(String(100))
    descripcion = Column(String(100))
    ruta = Column(String(100))
