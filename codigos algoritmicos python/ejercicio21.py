print("clasificar edad")
edad= int(input("ingrese edad:  "))
if(edad in range(0,12)):
    print("niño")
elif(edad in range(13,17)):
    print("adolescente")
elif(edad in range(18,59)):
    print("adulto")
elif(edad in range(60,100)):
    print("adulto mayor")
else:
    print("Ya esta muerto")