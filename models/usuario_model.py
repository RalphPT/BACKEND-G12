from config import conexion
from sqlalchemy import Column, types
from enum import Enum

class SexoUsuario(Enum):
    MASCULINO = 'MASCULINO'
    FEMENINO = 'FEMENINO'
    OTRO = 'OTRO'

class TipoUsuario(Enum):
    ADMINISTRADOR = 'ADMINISTRADOR'
    MEDICO = 'MEDICO'
    USUARIO = 'USUARIO'

class Usuario(conexion.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.Text, nullable=False)
    apellido = Column(type_=types.Text)
    #especialidad no puede ser nula
    especialidad = Column(type_=types.Text, nullable=False)
    # sexo > enum
    sexo = Column(type_=types.Enum(SexoUsuario), nullable=False)
    # celular > si puede ser nulo
    celular = Column(type_=types.Text)
    # consultorio > no puede ser nulo
    consultorio = Column(type_=types.Text, nullable=False)
    # email > no puede ser nulo y tiene que ser obligatorio
    email = Column(type_=types.Text, nullable=False, unique=True)
    # password > puede ser nulo
    password = Column(type_=types.Text)
    # tipoUsuario > se debe llamar en la bd tipo_usuario y solamente con ese enum (ADMIN, USUARIO Y MEDICO)
    tipoUsuario = Column(type_=types.Enum(TipoUsuario), default=TipoUsuario.USUARIO, name='tipo_usuario')

    
    # nombre de la tabla usuarios
    __tablename__ = 'usuarios'