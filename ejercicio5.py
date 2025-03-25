import sys  # Importa el módulo sys para manejar argumentos desde la terminal.

def descomponer_ip(ip):  
    """Función que descompone una dirección IP en sus cuatro octetos y los imprime."""
    octetos = ip.split('.')  # Divide la dirección IP en una lista de cuatro partes usando el punto como separador.
    
    # Recorre cada octeto con su índice (comenzando desde 1)
    for i, octeto in enumerate(octetos, start=1):  
        print(f"Octeto {i}: {octeto}")  # Muestra cada octeto con su número correspondiente.

# Este bloque asegura que el código solo se ejecute si el script es ejecutado directamente.
if __name__ == "__main__":  
    # sys.argv es una lista con los argumentos pasados en la línea de comandos.
    # sys.argv[0] es el nombre del script, sys.argv[1] es la dirección IP proporcionada por el usuario.
    if len(sys.argv) != 2:  
        print("Uso: python ejercicio5.py <dirección IP>")  # Mensaje de uso si no se proporciona una IP.
        sys.exit(1)  # Termina el script con un código de error.

    direccion_ip = sys.argv[1]  # Obtiene la dirección IP ingresada por el usuario.
    
    descomponer_ip(direccion_ip)  # Llama a la función para mostrar los octetos.

        
