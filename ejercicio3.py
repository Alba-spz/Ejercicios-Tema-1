l1=["manzana","pera","sandia","fresa","platano","cereza","kiwi","limon", "manzana"]
l2=["naranja","papaya","melocoton","cereza","fresa","uva","manzana","platano"]
lista_nueva=[]
for i in l1:
    if i in l2 and i not in lista_nueva: #Hay que indicar 'and i not in lista_nueva' pq si no lo hacemos y hay un elemento que se repite más de una vez en alguna de las listas, se añadirá a la lista nueva tantas veces como se repita en la lista original
        lista_nueva.append(i)
print(lista_nueva)

#Otra forma:
l1=["manzana","pera","sandia","fresa","platano","cereza","kiwi","limon", "manzana"]
l2=["naranja","papaya","melocoton","cereza","fresa","uva","manzana","platano"]
l1=set(l1)
l2=set(l2)
lista_nueva=l1&l2
print(lista_nueva)