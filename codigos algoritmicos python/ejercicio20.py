print("validar usuatrio y contraseña")
usuario= input("ingrese usuario:  ")
contraseña= input("ingrese contraseña:  ")
if(usuario=="admin" and contraseña=="1234"):
    print("acceso concedido")
elif(usuario!="admin" and contraseña=="1234"):
        print("usuario incorrecto")
elif(usuario=="admin" and contraseña!="1234"):
        print("contraseña incorrecta")
else:
        print("usuario y contraseña incorrectos")
        