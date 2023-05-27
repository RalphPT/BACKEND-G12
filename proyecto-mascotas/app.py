from flask import Flask
from base_de_datos import conexion
from flask_migrate import Migrate
from models.usuarios_models import UsuarioModel
from models.mascotas_model import MascotasModel

app = Flask(__name__)
# dialecto://username:password@host:port/db_name
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/mascotas'

# Utilizamos la variable de conexion a la base de datos para setearla en nuestra conexion de sql alchemy
conexion.init_app(app)

Migrate(app, conexion)


if __name__ == '__main__':
    app.run(debug = True)