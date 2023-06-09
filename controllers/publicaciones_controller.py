from flask_restful import Resource, request
from models.publicacion_model import Publicacion
from config import conexion
from flask_jwt_extended import get_jwt_identity, jwt_required
from dtos.publicacion_dto import PublicacionRequestDto, PublicacionesResponseDto
from models.usuario_model import Usuario

class PublicacionesController(Resource):
    @jwt_required()
    def post(self):
        usuarioId = get_jwt_identity()
        dto = PublicacionRequestDto()
        try:
            dataValidada = dto.load(request.json)
            nuevaPublicacion = Publicacion(**dataValidada, usuarioId = usuarioId)

            conexion.session.add(nuevaPublicacion)
            conexion.session.commit()

            dtoRespuesta = PublicacionesResponseDto()
            resultado = dtoRespuesta.dump(nuevaPublicacion)
            return{
                'message': 'Publicacion creada exitosamente',
                'content': resultado
            }, 201
        
        except Exception as e:
            conexion.session.rollback()
            return{
                'message': 'Error al crear la publicacion',
                'content': e.args
            }, 400
        
    def get(self):
        #devolver todas las publicaciones que hay
        # No se recomienda utilizar la siguiente forma ya que pertenece al "LEgacy de SQLAlchemy" por lo que pronto puede estar en desuso
        #resultado = Publicacion.query.all()
        #conexion.session.query(Publicacion).all()
        #return{
        #   'content': None
        #}
        try:

            queryParams =request.args
            #REDUNDANTE
            # filtros = {}
            # if(queryParams.get('email')):
            #     filtros['email'] = queryParams.get('email')
            #--------------------------------------------------

            # SOlamente necesito el ID
            # with_entities > especificar que columns queremos extraer
            # SELECT * FROM ...
            # con el uso de with_entities
            # SELECT id, nombre FROM usuarios
            data = conexion.session.query(Usuario).with_entities(Usuario.id).filter_by(**queryParams).all() # => [(1,)] >arreglo de listas no puede pasar a usuariosIds
            # data > [(1,), (2,)]
            usuariosIds = [] # Aqui se guarda la lista de usuarios Ids y pasa la info al metodo in que está señalada en "<==="
            for id in data: # iteramos la tupla de data, para obtener el id a buscar, transformandolo esto [(1), (2)] a [1, 2]
                usuariosIds.append(id[0])

            # SELECT *FROM publicaciones WHERE usuarioId = ...
            # SELECT * FROM Publicaciones WHERE usuario_id IN (1, 2);
            #https://www.postgresql.org/docs/current/functions-subquery.html#FUNCTIONS-SUBQUERY-IN
            resultado = conexion.session.query(Publicacion).filter(Publicacion.usuarioId.in_(usuariosIds)).all() # <===

            dtoRespuesta = PublicacionesResponseDto(many=True)
            publicaciones = dtoRespuesta.dump(resultado)

            return {
                'message': 'Lista de publicaciones obtenida exitosamente',
                'content': publicaciones
            }, 200

        except Exception as e:
            return {
                'message': 'Error al obtener las publicaciones',
                'content': str(e)
            }, 500

class PublicacionController(Resource):
    # SE encarga de 1. Validar que la token sea nuestra (concuerda el secreto), 2. De que la token aun no expiró, 3. Sea valida
    @jwt_required()
    # /publicacion/<int:id>
    def put(self, id):
        try:
            usuarioId = get_jwt_identity()
            # Buscar la publicacion segun el id y segun el usuarioId
            # SELECT * FROM publicaciones WHERE id=... AND usuario_id=...
            publicacion = Publicacion.query.filter_by(id=id, usuarioId=usuarioId).first()
            # publicacion = conexion.session.query(Publicacion).filter(Publicacion.id == id, Publicacion.usuarioId == usuarioId). first()
            if not publicacion:
                raise Exception('Publicacion no existe')
            
            dto = PublicacionesResponseDto()
            dataValidada = dto.load(request.json)

            # Primera forma
            #publicacion.titulo = dataValidada.get('titulo')
            #publicacion.descripcion = dataValidada.get('descripcion')
            #publicacion.habilitado = dataValidada.get('habilitado')

            # Segunda forma https://docs.sqlalchemy.org/en/20/orm/queryguide/query.html#sqlalchemy.orm.Query.update
            # Retornará la cantidad de registros actualizados
            conexion.session.query(Publicacion).filter_by(id=id, usuarioId=usuarioId).update(dataValidada) # los ** convierte el diccionario en un parametro
            
            # Para guardar los cambios de manera permanente
            conexion.session.commit()
            resultado = PublicacionesResponseDto().dump(publicacion) #Esta devolviendo valor actualizado
            print(publicacion.titulo)
            return{
                'message': 'Publicacion actualizada exitosamente',
                'content': resultado
            }, 201
        except Exception as e:
            return{
                'message': 'Error al actualizar la publicacion',
                'content': e.args
            }, 400
    @jwt_required()
    def delete(self, id):
        try:
            usuarioId = get_jwt_identity()
            #Eliminar publicacion usando el delete
            publicacionesEliminadas = conexion.session.query(Publicacion).filter_by(id=id, usuarioId=usuarioId).delete()

            if publicacionesEliminadas == 0:
                raise Exception('No se encontro la publicacion a eliminar')
            
            conexion.session.commit()

            # Segunda Forma
            # publicacionEncontrada = conexion.session.query(Publicacion).filter_by(id=id, usuarioId=usuarioId).first()
            # if not publicacionEncontrada:
            #     raise Exception('No se encontro la publicacion a eliminar')
            
            # conexion.session.delete(publicacionEncontrada)
            # conexion.session.commit()

            return{
                'message': 'Publicacion eliminada exitosamente'
            }
        except Exception as e:
            return{
                'message': 'Error al eliminar la publicacion',
                'content': e.args
            }, 400