console.log("descuento")
precio= 120000;
des= precio * 0.10;
total= precio - des;
if(precio>=100000){
    console.log("el precio es: "+precio);
    console.log("el descuento es: "+des);
    console.log("el total a pagar es: "+total);
}
else{
    console.log("El valor no supera los 100000, no se aplica el descuento");
}