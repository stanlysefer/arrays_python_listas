# No. 76: Suma de los elementos de la diagonal principal.

import random
suma = 0
M = []
# input
m = int(input("Filas de la matriz: "))
n = int(input("Columnas de la matriz: "))
# processing
for i in range(m):
    M.append([])
    for j in range(n):
        M[i].append(random.randint(1,9))

for k in range(m):
    for j in range(n):
        print(M[k][j], end=" ")
    print()

if m == n:
    for i in range(m):
        for j in range(n):
            if i == j:
                suma = suma + M[i][j]
    print("Resultado de la traza:", suma) # output
else:
    print("No existe una diagonal principal") # output