console.log("solicitar lados e indicar tipo de triángulo");
lado1=12;
lado2=12;
lado3=12;
if(lado1==lado2 && lado2==lado3){
    console.log("Triángulo equilátero");
} else if(lado1==lado2 || lado1==lado3 || lado2==lado3){
    console.log("Triángulo isósceles");
} else {
    console.log("Triángulo escaleno");
}