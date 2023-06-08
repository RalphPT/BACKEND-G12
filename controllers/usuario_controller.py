from flask_restful import Resource, request
from models.usuario_model import Usuario
from config import conexion
from dtos.usuario_dto import RegistroUsuarioRequestDto, LoginUsuarioRequestDto, UsuarioResponseDto
from bcrypt import gensalt, hashpw, checkpw
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

class RegistroController(Resource):
    def post(self):
        data = request.json
        dto = RegistroUsuarioRequestDto()
        try:
            dataValidada = dto.load(data)
            password = bytes(dataValidada.get('password'), 'utf-8')
            # salt > es un texto creado aleatoriamente que se combinará con el password y con ello saldra el hash del password
            salt = gensalt()
            # hashpw > mezcla el password con el salt generado para darnos el hash de la contrasena
            hash = hashpw(password, salt)
            hashString = hash.decode('utf-8')
            print(hashString)
            # sobrescribimos en el diccionario de la data validada la nueva password hasheada
            dataValidada['password'] = hashString

            nuevoUsuario = Usuario(**dataValidada)
            conexion.session.add(nuevoUsuario)
            conexion.session.commit()

            return{
                'message': 'Usuario creado exitosamente'
            }
        except Exception as e:
            conexion.session.rollback()
            return{
                'message': 'Error al crear el usuario',
                'content': e.args
            }, 400 #mala solicitud
        

class LoginController(Resource):
    def post(self):
        dto = LoginUsuarioRequestDto()
        data = request.json
        try:
            dataValidada = dto.load(data)
            usuarioEncontrado = conexion.session.query(Usuario).filter_by(email = dataValidada.get('email')).first()
            print(usuarioEncontrado)
            if not usuarioEncontrado:
                raise Exception('Usuario con correo {} no existe'.format(dataValidada.get('email')))
            password = bytes(dataValidada.get('password'), 'utf-8')
            passwordHashed = bytes(usuarioEncontrado.password, 'utf-8')
            # el metodo checkpw sirve para validar si la contraseña es la misma que la que tenemos hasheada en la BD, recordemas que la contraseña guardada está hasheada (combinada con un texto aleatorio)
            resultado = checkpw(password, passwordHashed)
            print(resultado)
            if resultado:
                #token de acceso 
                token = create_access_token(identity=usuarioEncontrado.id) # SE RECOMIENDA EL ID O CAMPO QUE NO SE REPITA POR TEMAS DE SEGURIDAD
                return{
                    'message': 'Bienvenido',
                    'content': token
                }
            else:
                raise Exception('Contrasena incorrecta')
            
        except Exception as e:
            return{
                'message': 'Error al hacer el login',
                'content': e.args
            }, 400
        

class PerfilController(Resource):
    # jwt_required > se colocara al comienzo de cada metodo para indicar que este metado tiene que solicitar la token y esta pasara por todo el proceso de validacion ( Si es una token valida, si es nuestra token, si tiene tiempo de vida(aun no caduco))
    @jwt_required()
    def get(self):
        identificador = get_jwt_identity()
        
        usuarioEncontrado = conexion.session.query(Usuario).filter_by(id= identificador).first()
        dto = UsuarioResponseDto()

        resultado = dto.dump(usuarioEncontrado)
        print(resultado)

        return{
            'content': resultado
        }