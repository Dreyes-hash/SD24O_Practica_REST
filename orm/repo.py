import orm.modelos as modelos 
from sqlalchemy.orm import Session

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
