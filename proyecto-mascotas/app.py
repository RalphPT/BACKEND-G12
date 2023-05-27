from flask import Flask
from base_de_datos import conexion
from flask_migrate import Migrate
from flask_restful import Api
from models.usuarios_models import UsuarioModel
from models.mascotas_model import MascotasModel
from controllers.usuario_controller import UsuarioController
from controllers.mascota_controller import MascotasController

app = Flask(__name__)
# estaremos agregando la liberia flask_restful a nuestro proyecto de flask
api = Api(app=app)
# dialecto://username:password@host:port/db_name
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/mascotas'

# Utilizamos la variable de conexion a la base de datos para setearla en nuestra conexion de sql alchemy
conexion.init_app(app)

# Aca inicializamosel proceso de migraciones 
Migrate(app, conexion)

# definir las rutas utilizando la clase Api
api.add_resource(UsuarioController, '/usuarios', '/otra_ruta_usuarios')
api.add_resource(MascotasController, '/mascotas')

if __name__ == '__main__':
    app.run(debug = True)