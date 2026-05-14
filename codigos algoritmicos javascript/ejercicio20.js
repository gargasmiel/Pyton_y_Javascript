console.log("validar usuario y contraseña");
usuario="admin";
contraseña="123456";
if (usuario=="admin" && contraseña=="123456"){
    console.log("Acceso concedido");
}
else if (usuario!="admin"){
    console.log("Usuario incorrecto");
}
else{
    console.log("Contraseña incorrecta");
}
