def SelectionSort(lista):
    n = len(lista)
    for i in range(n):

        indexMinimo = i
        for k in range(i, n):
            if lista[k] < lista(indexMinimo):
                indexMinimo = k
        lista[i], lista[indexMinimo] = lista[indexMinimo], lista[i]
    
    return lista