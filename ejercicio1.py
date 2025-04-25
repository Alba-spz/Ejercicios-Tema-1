def procesar_cadena(cadena):
    try:
        # Verifica si la cadena está vacía
        if not cadena:
            raise ValueError("La cadena está vacía.")  # Lanza un error si la cadena está vacía

        # Invierte la cadena
        cadena_invertida = cadena[::-1]

        # Verifica si la cadena invertida contiene al menos un espacio
        if " " not in cadena_invertida:
            raise ValueError("La cadena no contiene el formato esperado con espacios.")  # Lanza un error si no hay espacios

        # Divide la cadena en dos partes desde el último espacio
        partes = cadena_invertida.rsplit(" ", 1)

        # Verifica si la división produjo exactamente dos partes
        if len(partes) != 2:
            raise ValueError("No se pudo separar la receta del número de calorías.")  # Lanza un error si no hay dos partes

        # Asigna las partes a variables
        nombre_de_la_receta, numero = partes

        # Verifica si la segunda parte es un número válido
        if not numero.isdigit():
            raise ValueError(f"El valor '{numero}' no es un número válido de calorías.")  # Lanza un error si no es un número

        # Imprime el resultado si todo está correcto
        print(f"La receta de {nombre_de_la_receta} contiene {numero} calorías")
    
    except ValueError as e:
        # Captura e imprime cualquier error que ocurra
        print(f"Error: {e}")

# Ejemplo correcto
cadena = "173 etalocohc ed atrat"  # Cadena de ejemplo válida
procesar_cadena(cadena)

# Ejemplo con error
cadena_mala = "sin calorias"  # Cadena de ejemplo inválida
procesar_cadena(cadena_mala)
