cadena="173 etalocohc ed atrat" 
cadena_invertida = cadena[::-1]
partes=cadena_invertida.rsplit(" ",1) 
#Las " " indican que la cadena se recorrerá hasta encontrar un espacio por el lado derecho y el 1 indica que solo se dividirá una vez, por lo que la cadena se dividirá en dos partes
nombre_de_la_receta, numero = partes
print(f"La receta de {nombre_de_la_receta} contiene {numero} calorias")

#Otra manera:
cadena="173 etalocohc ed atrat"
cadena_invertida = cadena[::-1]
partes=cadena_invertida.split(" ") 
#Se crea una lista dividida en el mismo nº de elementos que palabras tenga la cadena, es decir, en este caso, 4 elementos
nombre_de_la_receta = " ".join(partes[:-1])
numero = partes[-1]
print(f"La receta de {nombre_de_la_receta} contiene {numero} calorias")