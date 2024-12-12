import orm.modelos as modelos 
from sqlalchemy.orm import Session
import orm.esquemas as esquemas

#genera la siguiente solicitud SQL al servidor 
#SELECT * FROM app.alumnos
def find_all_alumnos(session: Session):
    return session.query(modelos.Alumno).all()


#genera la siguiente solicitud SQL al servidor 
#SELECT * FROM app.alumnos WHERE id={id_al}
def find_alumno_biID(session: Session, id_alumno:int):
    return session.query(modelos.Alumno).filter(modelos.Alumno.id == id_alumno).first()


#genera la siguiente solicitud SQL al servidor 
#SELECT * FROM app.fotos
def find_all_fotos(session: Session):
    return session.query(modelos.Foto).all()


#genera la siguiente solicitud SQL al servidor 
#SELECT * FROM app.fotos WHERE id={id_fo}
def find_foto_byID(session: Session, id_foto:int):
    return session.query(modelos.Foto).filter(modelos.Foto.id == id_foto).first()


#genera la siguiente solicitud SQL al servidor 
#SELECT * FROM app.fotos WHERE id_alumnos={id_al}
def find_fotos_by_alumnoID(session: Session, id_alumno: int):
    return session.query(modelos.Foto).filter(modelos.Foto.id_alumno == id_alumno).all()


#genera la siguiente solicitud SQL al servidor 
#SELECT * FROM app.calificaciones
def find_all_calificaciones(session: Session):
    return session.query(modelos.Calificacion).all()


#genera la siguiente solicitud SQL al servidor 
#SELECT * FROM app.calificaciones WHERE id={id_ca}
def find_calificacion_byID(session: Session, id_calificacion):
    return session.query(modelos.Calificacion).filter(modelos.Calificacion.id == id_calificacion).first()


#genera la siguiente solicitud SQL al servidor 
#SELECT * FROM app.calificaciones WHERE id_alumnos={id_al}
def find_calificaciones_by_alumnoID(session: Session, id_alumno: int):
    return session.query(modelos.Calificacion).filter(modelos.Calificacion.id_alumno == id_alumno).all()


#genera la siguiente solicitud SQL al servidor 
#DELETE FROM app.alumnos WHERE id_alumnos={id_al}
def del_alumnos_byID(session: Session, id_alumno: int):
    alumno = find_alumno_biID(session, id_alumno)
    if alumno is not None:
        del_calificaciones_by_alumnoID(session,id_alumno)
        del_fotos_by_alumnoID(session, id_alumno)
        session.delete(alumno)
        session.commit()
    respuesta = {
            "mensaje" : "alumno eliminado"
        }
    return respuesta

#genera la siguiente solicitud SQL al servidor 
#DELETE FROM app.fotos WHERE id_alumnos={id_al}

def del_fotos_by_alumnoID(session: Session, id_alumno:int):
    fotos = find_fotos_by_alumnoID(session, id_alumno)
    if fotos is not None:
        for foto in fotos:
            session.delete(foto)
        session.commit()
    respuesta = {
            "mensaje" : "fotos del alumno eliminadas"
        }
    return respuesta

#genera la siguiente solicitud SQL al servidor 
#DELETE FROM app.calificaciones WHERE id_alumnos={id_al}
def del_calificaciones_by_alumnoID(session: Session, id_alumno:int):
    calificaciones = find_calificaciones_by_alumnoID(session, id_alumno)
    if calificaciones is not None:
        for calificacion in calificaciones:
            session.delete(calificacion)
        session.commit()
    
    respuesta = {
            "mensaje" : "calificaciones eliminadas"
        }
    return respuesta


#genera la siguiente solicitud SQL al servidor 
#DELETE FROM app.fotos WHERE id_foto={id_fo}
def del_foto_byID(session: Session, id_foto:int):
    foto = find_foto_byID(session, id_foto)
    if foto is not None:
        session.delete(foto)
        session.commit()
    respuesta = {
            "mensaje" : "foto eliminada"
        }
    return respuesta


#genera la siguiente solicitud SQL al servidor 
#DELETE FROM app.fotos WHERE id_foto={id_fo}
def del_calificacion_byID(session: Session, id_calificacion:int):
    calificacion = find_calificacion_byID(session, id_calificacion)
    if calificacion is not None:
        session.delete(calificacion)
        session.commit()
    respuesta = {
            "mensaje" : "calificacion eliminada"
        }
    return respuesta

#nuevo alumno
def add_alumno(session:Session, nuevo_alumno: esquemas.AlumnoBase):
    alumno_bd = modelos.Alumno(
        nombre = nuevo_alumno.nombre,
        edad = nuevo_alumno.edad,
        domicilio = nuevo_alumno.domicilio,
        carrera = nuevo_alumno.carrera,
        trimestre = nuevo_alumno.trimestre,
        email = nuevo_alumno.email,
        password = nuevo_alumno.password
    )
    session.add(alumno_bd)
    session.commit()
    session.refresh(alumno_bd)
    return alumno_bd

#actualiza alumno
def upd_alumno(session:Session, info_alumno: esquemas.AlumnoBase, id_alumno:int):
    alumno_bd = find_alumno_biID(session, id_alumno)
    if alumno_bd is not None:
        alumno_bd.nombre = info_alumno.nombre
        alumno_bd.edad = info_alumno.edad
        alumno_bd.carrera = info_alumno.carrera
        alumno_bd.domicilio = info_alumno.domicilio
        alumno_bd.email = info_alumno.email
        alumno_bd.password = info_alumno.password
        alumno_bd.trimestre = info_alumno.trimestre
        session.commit()
        session.refresh(alumno_bd)
        return info_alumno
    else:
        respuesta = {
            "mensaje" : "el alumno no existe"
        }
        return respuesta
    
#nueva calificacion    
def add_calificacion_alumno(session:Session, nueva_calificacion: esquemas.CalificacionBase, id_alumno:int):
    alumno_bd = find_alumno_biID(session, id_alumno)
    if alumno_bd is not None:
        calificacion_bd = modelos.Calificacion(
            id_alumno = alumno_bd.id,
            uea = nueva_calificacion.uea,
            calificacion = nueva_calificacion.calificacion
        )
        session.add(calificacion_bd)
        session.commit()
        session.refresh(calificacion_bd)
        return calificacion_bd
    else:
        respuesta = {
            "mensaje" : "el id de alumno no existe"
        }
        return respuesta
    
#actualiza calificacion
def upd_calificacion(session:Session, info_calificacion:esquemas.CalificacionBase, id_calificacion:int):
    calificacion_bd = find_calificacion_byID(session,id_calificacion)
    if calificacion_bd is not None:
        calificacion_bd.uea = info_calificacion.uea,
        calificacion_bd.calificacion = info_calificacion.calificacion
        session.commit()
        session.refresh(calificacion_bd)
        return info_calificacion
    else:
        respuesta = {
            "mensaje" : "la calificacion no existe"
        }
        return respuesta

#nueva foto
def add_foto_alumno(session:Session, info_foto:esquemas.FotoBase, id_alumno:int):
    alumno = find_alumno_biID(session, id_alumno)
    if alumno is not None:
        foto_bd = modelos.Foto(
            id_alumno = alumno.id,
            titulo = info_foto.titulo,
            descripcion = info_foto.descripcion,
            ruta = info_foto.ruta
        )
        session.add(foto_bd)
        session.commit()
        session.refresh(foto_bd)
        return foto_bd
    else:
        respuesta = {
            "mensaje" : "el id de alumno no existe"
        }
        return respuesta
    
#actualiza foto    
def upd_foto(session:Session, info_foto:esquemas.FotoBase, id_foto:int):
    foto_bd = find_foto_byID(session,id_foto)
    if foto_bd is not None:
        foto_bd.ruta = info_foto.ruta,
        foto_bd.titulo = info_foto.titulo,
        foto_bd.descripcion = info_foto.descripcion
        session.commit()
        session.refresh(foto_bd)
        return info_foto
    else:
        respuesta = {
            "mensaje" : "el id de la foto no existe"
        }
        return respuesta

