def agregar_item(inventario, item):
    # Verifica si el ítem ya existe en el inventario
    if item in inventario:
        # Si el ítem ya está en el inventario, lanza un error ValueError
        raise ValueError(f"El ítem '{item}' ya está en el inventario.")
    
    # Si el ítem no está en el inventario, lo agrega
    inventario.append(item)
    
    # Retorna un mensaje indicando que el ítem ha sido añadido (esto es opcional)
    return f"El ítem '{item}' ha sido añadido al inventario."


# Ejemplo de uso
inventario = ["manzana", "banana", "naranja"]

# Intentamos agregar un ítem al inventario
try:
    print(agregar_item(inventario, "pera"))  # Añadir un nuevo ítem
    print(agregar_item(inventario, "manzana"))  # Intentar agregar un ítem repetido
except ValueError as e:
    print(e)  # Capturamos y mostramos el error si el ítem ya existe
