# listas (arrays)
notas = [10, 20, 25, 80]

variada = [10, 'Francisco', 70.5, True, [1, 2, 3]]

print(notas [0])

# Si queremos ingresar una nueva posición no se le coloca como asignación
# notas[4] = 40

# Se utiliza el metodo append
# En JS es push, en python es append
notas.append(40)

del notas[1]

print(notas)
# Es que el pop lo quita de la lista PERO nos devuelve el contenido eliminado.
nota_eliminada = notas.pop(1)
print(notas)
print(nota_eliminada)

# le pasamos el contenido que queremos eliminar, y si existe lo eliminará, caso contrario lanzará error
notas.remove(80)

# tupla
alumnos = ('Eduardo', 'Roberto', 'Juana', 'Roxana')
# la diferencia es que la tupla no se puede modificar (inmutable)
# la tupla se usa para definir valores que nunca se modificarán en todo el ciclo de nuestro proyecto

print(alumnos[0])
#alumnos[0] = 'Pepito'

# set (conjuntos)
# que es desordenada y almacena la información pero de manera desordenada y sin respetar indices
mascotas = { 'fido', 'iguana', 'gato' }
print(mascotas)
print(len(mascotas))
mascotas.add('mocha')
mascota_eliminada = mascotas.pop()

print(mascota_eliminada)

# diccionarios
# es ordenada pero por llaves ( no por posiciones)
persona = {
    'nombre': 'rafael',
    'apellido': 'percca',
    'sexo': 'masculino',
    'hobbies': ['Jugar videojuegos', 'Leer libros']
}

print(persona['nombre'])
print(persona.get('nacionalidad', 'NO EXISTE!!!!!'))
print(persona.get('hobbies', 'NO EXISTE!!!!!'))

