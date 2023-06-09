from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.publicacion_model import Publicacion

class PublicacionRequestDto(SQLAlchemyAutoSchema):
    class Meta:
        model = Publicacion

class PublicacionesResponseDto(SQLAlchemyAutoSchema):
    class Meta:
        model = Publicacion