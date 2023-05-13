def sumar(num1, num2):
    print(num1 + num2)
sumar(10, 50)

def saludar():
    print('HOLA!')

saludar()

def devolver_resta(num1, num2):
    return num1 - num2

resultado = devolver_resta(10,50)

print(resultado)

saludar()
saludar()
saludar()
saludar()
saludar()

resultado = devolver_resta(num2=80, num1=10)
print(resultado)


def multiplicar(num1, num2, num3):
    return num1 * num2 * num3
data = {
    'num1': 10,
    'num2': 40,
    'num3': 55
}

resultado = multiplicar(data.get('num1'), data.get('num2'), data.get('num3'))
print(resultado)

# destructurando el diccionario y le estoy pasando la data como si fueran los parámetros
# nume1=10, num2=40, num3=55
resultado = multiplicar(**data)
print(resultado)


# * > n argumentos
def personas(*gente):
    print(gente)

personas('Eduardo', 'Ricardo', 'Jose', 'Carlos', 'Raul')
personas('Maria', 'Ruth')
personas('Eusebio')

# ** > n argumentos PERO indicaremos el nombre del parametro y su valor y esto se almacenara en un diccionario
def usuarios(**params):
    print(params)


usuarios(nombre='Eduardo', edad=30, sexo='Masculino', nacionalidad='peruano')

usuarios(direccion='Las Begonias 113', apellido='Juarez', hobbies=['Jugar CS-GO', 'Montar Bici', 'Preparar jugos'])