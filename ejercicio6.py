def clasificar_personajes(personajes):
    humanos = []
    no_humanos = []

    for personaje in personajes:
        if personaje['tipo'] == 'humano':
            humanos.append(personaje)
        else:
            no_humanos.append(personaje)

    # Ordena la lista de humanos alfabéticamente según el nombre del personaje
    humanos.sort(key=lambda x: x['nombre'])

    # Ordena la lista de no humanos alfabéticamente según el nombre del personaje
    no_humanos.sort(key=lambda x: x['nombre'])

    return humanos, no_humanos

# Ejemplo de uso
personajes = [
    {'nombre': 'Mario', 'tipo': 'humano'},
    {'nombre': 'Luigi', 'tipo': 'humano'},
    {'nombre': 'Bowser', 'tipo': 'no humano'},
    {'nombre': 'Yoshi', 'tipo': 'no humano'}
]

humanos, no_humanos = clasificar_personajes(personajes)
print("Humanos:", humanos)
print("No humanos:", no_humanos)
