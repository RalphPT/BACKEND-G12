from models.mascotas_model import MascotasModel
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class MascotaRequestDto(SQLAlchemyAutoSchema):
    class Meta:
        model = MascotasModel
        # indicamos al DTO que también haga la validacion de las columnas que sean llaves foraneas
        include_fk = True