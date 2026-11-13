variable = input("ingrese un texto: \n")

if(len(variable) >= 8):
    print("tamaño del texto correcto")
else:
    print("tamaño debe ser mayor o igual a 8")

_______________________________________________

variable = " H    O   L A "
variable = variable.replace(" ","")
print(len(variable))
print(variable)

________________________________________________

variable = 0
while(variable == 0):
    try:
        variable = int(input("ingrese una opcion: \n"))
    except:
        print("ha ocurrido un error")
        variable = 0

_________________________________________________

#maxino 10 elementos
lista = [1,2,3,4,5]
while(True):
    variable = int(input("ingrese un elemento numerico: \n"))
    if (len(lista) < 10):
        lista.append(variable)
        print(lista)

_________________________________________________

try:
    variable = int(input("ingrese un numero\n"))
except:
    print("ha ocurrido un error")