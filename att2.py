def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        indeci_menor = i
        print("primeiro menor:", lista[indeci_menor])
        for j in range(i + 1, n):
            if lista[j] < lista[indeci_menor]:
                indeci_menor = j
                print("achou o menor numero", lista[indeci_menor])
        if indeci_menor != i:
            lista[i], lista[indeci_menor] = lista[indeci_menor], lista[i]
    return lista

numero = [85, 95, 65, 60, 81, 63]
print("lista ordenada com selection sort", selection_sort(numero))