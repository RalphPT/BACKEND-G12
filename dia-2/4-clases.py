from datetime import datetime

class Persona:
    #ATRIBUTOS
    nombre = 'Juan'
    edad = 28
    correo = 'jperez@gmail.com'
    peso = 89.5
    #METODOS
    def decir_hora(self): # SELF = THIS
        hora_actual = datetime.now()
        data = hora_actual.strftime('%I-%p')
        hora, turno = data.split('-')
        #print(hora)
        #print(turno)
        if turno == 'PM':
            print('Son las {} de la noche'.format(hora))
        else:
            print('Son las {} de la mañana'.format(hora))
            
        print(hora_actual.strftime('%I-%p'))
        print('Son las 10 de la noche')

    def saludar(self):
        print('Hola! Soy {}'.format(self.nombre))

# variable pasa a llamarse instancia (copia de la clase que sera almacenada en esa variable)

personal = Persona()
personal.nombre='Roberto'
personal.saludar()
print(personal.nombre)

persona2 = Persona()
print(persona2.nombre)
persona2.decir_hora()