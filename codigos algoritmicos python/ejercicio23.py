
salario = float(input("Ingrese salario base: "))
horas_extra = int(input("Ingrese horas extra: "))

if salario > 0:
    
    if horas_extra >= 0:
        
        valor_hora = salario / 240
        valor_hora_extra = valor_hora * 1.5
        
        pago_extra = horas_extra * valor_hora_extra
        
        salario_total = salario + pago_extra
        
        print("Salario base:", salario)
        print("Pago extra:", pago_extra)
        print("Salario total:", salario_total)
    
    else:
        print("Las horas extra no pueden ser negativas")

else:
    print("El salario debe ser mayor a 0")

