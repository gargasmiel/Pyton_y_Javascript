print("solicitar lados e indicar tipo de triangulo")
lado1= float(input("ingrese lado1:  "))
lado2= float(input("ingrese lado 2:  "))
lado3= float(input("ingrese hipotenusa:  "))
if(lado1==lado2 and lado2==lado3):
    print("el triangulo es equilatero")
    
elif(lado1==lado2 or lado2==lado3 or lado1==lado3):
    print("el triangulo es isosceles")
    
else:
    print("el triangulo es escaleno")

