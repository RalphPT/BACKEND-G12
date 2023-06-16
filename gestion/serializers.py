#https://www.django-rest-framework.org/api-guide/serializers/
from rest_framework import serializers
from .models import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    #https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
    class Meta:
        model = Categoria
        # sirve para indicar que campos del modelo queremos usar
        # fields = ['id', 'nombre']
        # exclude = ['nombre', 'piso'] # utilizar todos los campos excepto el nombre y el piso
        fields = '__all__'