from sqlalchemy import Column, ForeignKey
from sqlalchemy import types
from base_de_datos import conexion
from enum import Enum

class SexoEnum(Enum):
    Macho = 'Macho'
    Hembra = 'Hembra'
    Otro = 'Otro'

class MascotasModel(conexion.Model):
    id = Column(autoincrement = True, type_ = types.Integer, primary_key = True)
    nombre = Column(type_ = types.Text, nullable = False)
    apellido = Column(type_ = types.Text, nullable = True)
    sexo = Column(type_ = types.Enum(SexoEnum), default = SexoEnum.Otro, nullable = False)
    # name > para indicar como queremos que se llame esta columna en la base de datos, si no le ponemos este parametro su nombre ser igual que el nombre del atributo
    fechaNacimiento = Column(type_ = types.Date, name = 'fecha_nacimiento',nullable = False)
    raza = Column(type_ = types.Text, nullable = True)
    # relacion nuestra tabla usuarios con mascotas
    usuarioId = Column(ForeignKey(column = 'usuarios.id'), type_ = types.Integer, name = 'usuario_id',nullable = False) # CAmbie el type y utilicé los siguientes comandos por un error > flask db stamp head,  flask db migrate, flask db upgrade

    __tablename__ = 'mascotas'