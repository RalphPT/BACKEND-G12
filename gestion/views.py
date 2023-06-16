#from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from django.http import HttpRequest
from rest_framework.views import APIView
from .serializers import CategoriaSerializer
from .models import Categoria
# SE USA RESPONSE DEBIDO AL ERROR EN EL POSTMAN
#AssertionError at /
#Expected a `Response`, `HttpResponse` or `HttpStreamingResponse` to be returned from the view, but received a `<class 'dict'>`


# variable: str > indicando el tipo de dato en caso que VScode u otro editor no sepa que tipo de dato puede ser
@api_view(['GET', 'POST'])
#https://www.django-rest-framework.org/api-guide/requests/ Httprequest
def saludar(request: Request | HttpRequest):
    #https://www.django-rest-framework.org/api-guide/requests/  Request
    print(request.method)
    return Response(data={
        'message': 'Bienvenido a mi API de librerias'
    })

class CategoriasController(APIView):
    # es exactamente igual que la clase Resource de flask restful
    def get(self, request):
        # SELECT * FROM categorias WHERE habilitado = true;
        categorias = Categoria.objects.filter(habilitado = True).all()
        print(categorias)

        # serializador para convertirlas a un diccionario
        resultado = CategoriaSerializer(instance=categorias, many=True)

        return Response(data={
            'message': 'Las categorias son',
            'content': resultado.data # data> encargado de devolver el diccionario
        })
    
    def post(self, request: Request | HttpRequest):
    # vamos a crear un dto > pasa a llamarse Serializador
        data = request.data
        serializador= CategoriaSerializer(data=data)
        try:
            serializador.is_valid(raise_exception=True)
            # si la validacion pasaexitosamente entonces se agregara la instancia del serializador el atributo validated_dataen la cual se almacenara nuestra informacion validada (corroborada)
            #dataCorroborada = validated_data
            print(serializador.validated_data)
            categoriaCreada = serializador.save()
            print(categoriaCreada)

            respuesta = CategoriaSerializer(instance=categoriaCreada)

            return Response(data={
                'message': 'Categoria creada exitosamente',
                'content': respuesta.data # data > convierte la instancia a un diccionario utilizando tipos de datos complejos
            })
        except Exception as err:
            return Response(data={
                'message': 'Error al crear la categoria',
                'content': err.args
            })
        
class CategoriaController(APIView):
    def get(self, request: Request | HttpRequest, id: int):
        print(id)
        # solamente mostrar si la categoria esta habilitada
        # SELECT * FROM categorias WHERE id = '...' AND habilitado = true;
        categoriaEncontrada = Categoria.objects.filter(id = id).first()

        if not categoriaEncontrada:
            return Response(data ={
                'message': 'Categoria no existe'
            })
        
        serializador = CategoriaSerializer(instance=categoriaEncontrada)

        return Response(data ={
            'content': serializador.data
        })