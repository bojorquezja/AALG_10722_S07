def calculo_vuelto(monto, tipo_moneda):
    resultado = []
    for valor in tipo_moneda:
        cantidad = int(monto // valor) 

        if cantidad > 0:
            resultado.append((cantidad, valor))
            monto -= cantidad * valor
            #print(monto)
            monto = monto + 0.000001

    return resultado



monto = float(input("Ingrese vuelto:\n"))

tipo_moneda = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05]

vuelto = calculo_vuelto(monto, tipo_moneda)

print("Vuelto para S/", monto)
for cantidad, valor in vuelto:
    print(f"{cantidad} de S/{valor}")