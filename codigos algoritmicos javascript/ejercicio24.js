console.log("Año bisiesto");

año = 2024;
if (año % 4 == 0) {

    if (año % 100 == 0) {

        if (año % 400 == 0) {
            console.log("El año es bisiesto");
        } else {
            console.log("El año no es bisiesto");
        }

    } else {
        console.log("El año es bisiesto");
    }

} else {
    console.log("El año no es bisiesto");
}