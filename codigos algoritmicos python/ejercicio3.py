y= int(input("Ingrese un número: "))
z= int(input("Ingrese otro número: "))
suma= y+z
resta= y-z
multiplicacion= y*z
divison= y/z
print("La suma de los números es: ", suma)
print("La resta de los números es: ", resta)        
print("La multiplicación de los números es: ", multiplicacion)
if divison == 0:
    print("error, no se puede dividir por cero")
else:
    print("La división de los números es: ", divison)
