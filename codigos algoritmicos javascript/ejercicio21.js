console.log("clasificar edad");
let edad = 15;
if (edad >= 0 && edad <= 12) {
    console.log("Niño");
} else if (edad >= 13 && edad <= 17) {
    console.log("Adolescente");
} else if (edad >= 18 && edad <= 59) {
    console.log("Adulto");
} else if (edad >= 65 && edad <= 100) {
    console.log("Anciano");
} else {
    console.log("Ya estás muerto");
}