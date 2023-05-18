# Se ingresa
edad = input('Ingresa tu edad:')
# hace la conversión hacia un entero
edad = int(edad)
#edad_numerica = int(edad)
# print(type(edad))
# print(type(edad_numerica))
# Se ingresa la edad de la persona y si es mayor de edad puede ingresar a la discoteca, caso contrario se llama a sus padres
# Si la persona tiene entre 40 y 60 años le ofreceremos un trago de cortesía aun asi no entre a la discoteca
#Si la persona tiene mas de 65 tampoco lo dejaremos ingresar porque ya es muy adulta (utilizar elif)

#Otra manera
if edad >= 18 and edad <= 64:
    print("Puedes ingresar a la discoteca.")
    if 40 <= edad <= 60:
        print("Se le ofrece un trago de cortesía.")
elif edad < 18:
    print("Llamaremos a sus padres.")
elif edad >= 65:
    print("NO puede ingresar, es de edad avanzada.")
print('--------------------------')
if edad > 65:
    print("NO puede ingresar, es de edad avanzada.")
elif edad >= 18:
    print("Puedes ingresar a la discoteca.")
    if 40 <= edad <= 60:
        print("Se le ofrece un trago de cortesía.")
elif edad < 18:
    print("Llamaremos a sus padres.")

# -------------------------------
numeros = [1, 10, 40, 50, 55, 3, 4, 9]

# En base al array de numeros indicar cuantos son menores de 15 y cuantos son mayores de 15

menores = 0
mayores = 0

for numero in numeros:
    print(numero)

    if numero < 15:
        menores +=1
        
    else:
        mayores +=1
        
print("Hay {} números menores de 15" .format(menores))
print(f"Hay {mayores} numeros mayores que 15")

n = 15
if n % 2 != 0:
    print("weird")
else:
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("not Weird")