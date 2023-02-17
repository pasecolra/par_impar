X = int(input("se ingresa un numero: "))

R = X%2

if R==0:
    msj="par "
else:
    msj="impar "
print("el numero " + str(X) + " es: " + msj)