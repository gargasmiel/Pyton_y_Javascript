console.log("Numeros en orden ascendente");
num1 = 1;
num2 = 20;
num3 = 5;
if (num1 < num2 && num1 < num3) {
    if (num2 < num3) {
        console.log(num1, num2, num3);
    } else {
        console.log(num1, num3, num2);
    }
}