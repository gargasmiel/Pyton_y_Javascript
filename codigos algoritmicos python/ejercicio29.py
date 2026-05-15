print("Cliente normal o cliente VIP?")

entradanormal = 100
entradavip = 200

entrada = int(input("Ingrese valor de la entrada a comprar: "))

if entrada >= entradavip:
    print("Usted obtiene una entrada VIP y un descuento del 20%")

else:

    if entrada >= entradanormal:
        print("Usted obtiene una entrada normal y un descuento del 5%")

    else:
        print("Valor de entrada no válido")