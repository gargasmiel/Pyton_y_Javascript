console.log("MENU DE OPCIONES");
console.log("1. saludar");
console.log("2. mostrar fecha");
console.log("3. salir");

let opciones = 2;

if (opciones == 1) {
    console.log("Hola, bienvenido al programa");
} else {

    if (opciones == 2) {
        let fecha = new Date();
        console.log("La fecha de hoy es 25/06/2024");
    } else {

        if (opciones == 3) {
            console.log("Saliendo del programa...");
        } else {
            console.log("Opción no válida");
        }

    }

}
