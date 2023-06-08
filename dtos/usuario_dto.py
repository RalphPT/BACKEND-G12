from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.usuario_model import Usuario
from marshmallow import Schema, fields

class RegistroUsuarioRequestDto(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario

# https://marshmallow.readthedocs.io/en/stable/
# https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html
# https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html#marshmallow.fields.Field

class LoginUsuarioRequestDto(Schema):
    email = fields.Email(required = True)
    password = fields.String(required = True)
