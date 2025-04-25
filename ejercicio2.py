# Definimos el capital inicial
capital_inicial = 1000

# Solicitamos al usuario la tasa de interés anual y la convertimos a un número flotante
tasa_interes = float(input("Introduce la tasa de interés anual (entre 1 y 10): "))

# Verificamos si la tasa de interés está dentro del rango permitido (entre 1% y 10%)
if tasa_interes < 1 or tasa_interes > 10:
    # Si la tasa no está en el rango, mostramos un mensaje de error
    print("La tasa de interés debe estar entre 1% y 10%")
else:
    # Si la tasa es válida, solicitamos al usuario el número de años
    anos = int(input("Introduce el nº de años: "))
    
    # Calculamos el capital final usando la fórmula del interés compuesto
    capital_final = capital_inicial * (1 + tasa_interes / 100) ** anos
    
    # Mostramos el capital final con dos decimales
    print(f"El capital final después de {anos} años será de {capital_final:.2f} euros")
