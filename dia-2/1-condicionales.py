nombre = 'Roxana'
apellido = 'Rodriguez'

if nombre == 'Roxana' and apellido == 'Rodriguez':
    print('Hola Roxana, cómo están tus cuyes?')
else:
    print('Hola Roxana, qué tal?')

nombre_completo = nombre +' '+ apellido
print(nombre_completo)

# recibir información por el teclado desde la terminal
ingreso = input()
print(ingreso)

dia = input('Ingrese el día de la semana: ')
# si el día es sabado indicar que es fin de semana, caso contrario indicar que ese día se trabaja
dia = dia.lower()
if dia == 'sabado':
    print('ES fin de semana')
elif dia == 'domingo':
    print('Es fin de semana y hay que lavar la ropa')
else:
    print('Hoy se trabaja')