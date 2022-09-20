def bubbleSort(arr):
    n = len(arr)
    # Si la lista ya esta ordenada, no es necesario pasar por todo el proceso
    swapped = False
    # Iterar la lista
    for i in range(n-1):
        # range(n) tambien funciona pero repetiria el proceso una vez mas
        # Ultimo i ya esta en su lugar
        for j in range(0, n-i-1):
 
            # Iterar desde 0 hasta n-i-1
            # Swap si el elemento encontrado es mayor que el sig elemento
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            # Si no necesitamos hacer ni un solo swap, podemos salir de lloop principal
            return
# Las dos listas que juntare para ordenar  
arr = []
arr2 = []
print("Vamos a crear dos listas de tamaño 5 (Este tamaño lo puede cambiar en le for de abajo)")
print("creando Lista 1")
for i in range(0,5):
    elem = int(input("inserte un entero: "))
    arr.append(elem)
print("Crrando la segunda lista")
for i in range(0,5):
   elem = int(input("inserte un entero: "))
   arr2.append(elem) 
arrJ = arr + arr2

bubbleSort(arrJ)
print("La lista ordenada de ambas listas es: ")
for i in range(len(arrJ)):
    print("% d" % arrJ[i],end = " ")