console.log("cliente normal o cliente vip");

entradanormal = 100;
entradavip = 200;
clientepaga = 99;

if (clientepaga >= entradanormal) {

    if (clientepaga >= entradavip) {
        console.log("Entrada VIP: descuento del 20%");
    } else {
        console.log("Entrada normal: descuento del 5%");
    }

} else {
    console.log("No alcanza para ninguna entrada");
}