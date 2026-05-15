console.log("Calcular salario total con horas extra");
salario =1500000;
horasExtra = 15;

if (salario > 0) {

    if (horasExtra >= 0) {

        let valorHora = salario / 240;
        let valorHoraExtra = valorHora * 1.5;

        let pagoExtra = horasExtra * valorHoraExtra;

        let salarioTotal = salario + pagoExtra;

        console.log("Salario base:", salario);
        console.log("Pago extra:", pagoExtra);
        console.log("Salario total:", salarioTotal);

    } else {
        console.log("Las horas extra no pueden ser negativas");
    }

} else {
    console.log("El salario debe ser mayor a 0");
}
