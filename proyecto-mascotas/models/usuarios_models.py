from sqlalchemy.schema import Column
from sqlalchemy import types
from base_de_datos import conexion

class UsuarioModel(conexion.Model):
    #https://docs.sqlalchemy.org/en/20/core/metadata.html#sqlalchemy.schema.Column
    #https://docs.sqlalchemy.org/en/20/core/type_basics.html#module-sqlalchemy.types
    id = Column(type_= types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.Text, nullable=False)
    apellido = Column(type_=types.Text)
    correo = Column(type_=types.Text, unique=True, nullable=False)
    dni = Column(type_=types.Text, unique=True, nullable=False)

    # Como se llamará la tabla en la base de datos si no le ponemos este nombre, será el mismo que la clase (UsuarioModel)
    __tablename__ = 'usuarios'