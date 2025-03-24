capital_inicial=1000
tasa_interes=float(input("Introduce la tasa de interés anual (entre 1 y 10): "))
if tasa_interes < 1 or tasa_interes > 10:
    print("La tasa de interés debe estar entre 1% y 10%")
else:
    anos=int(input("Introduce el nº de años: "))
    capital_final=capital_inicial*(1+tasa_interes/100)**anos
    print(f"El capital final después de {anos} años será de {capital_final:.2f} euros")
