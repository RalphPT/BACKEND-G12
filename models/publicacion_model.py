from sqlalchemy import Column, types, ForeignKey
from config import conexion

class Publicacion(conexion.Model):
    #id
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    #titulo> not null
    titulo = Column(type_=types.Text, nullable=False)
    # descripcion > si puede ser null
    descripcion = Column(type_=types.Text)
    # habilitado > por defecto sea True
    habilitado = Column(type_=types.Boolean, default=True)
    # usuarioId > en la bd se llame usuario_id y que no sea null
    usuarioId = Column(ForeignKey(column = 'usuarios.id'),type_=types.Integer, name='usuario_id', nullable=False)
    # nombre de la tabla publicaciones
    __tablename__ = 'publicaciones'