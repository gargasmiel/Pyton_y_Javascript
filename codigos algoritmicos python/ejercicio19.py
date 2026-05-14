print("mostrar impuestos de ingresos")
salario= float(input("ingrese salario:  "))

if(salario<1500000):
        impuesto=0 
        
elif(salario<=3000000):
        
    impuesto=salario*0.10

else:
    impuesto=salario*0.20
    
neto=salario-impuesto

print("el salario es: ",salario)
print("el impuesto a pagar es: ",impuesto)
print("el salario neto es: ",neto)