console.log("solicitar lados e indicar tipo de triángulo");
lado1=14;
lado2=7;
lado3=7;
if(lado1==lado2 && lado2==lado3){
    console.log("Triángulo equilátero");
}else if(lado1==lado2 || lado1==lado3 || lado2==lado3){
    console.log("Triángulo isósceles");
}else{
    console.log("Triángulo escaleno");
}