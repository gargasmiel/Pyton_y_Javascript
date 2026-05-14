print("descuento")
precio= float(input("ingrese el valor de la compra: "))
des= precio*0.10
total= precio-des
if (precio>=100000):
    print("el descuento es: ", des)
    print("el total a pagar es: ", total)
else:    
    print("no tiene descuento") 
    print("el total a pagar es: ", precio)