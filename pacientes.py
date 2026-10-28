import csv


with open('pacientes - pacientes.csv', mode='r', encoding='utf-8') as archivo:
    lector = csv.reader(archivo)
    encabezado = next(lector)  
    filas = list(lector)       

columna_a_ordenar = 1 
n = len(filas)

for i in range(n):
    for j in range(0, n - i - 1):
        if filas[j][columna_a_ordenar] > filas[j + 1][columna_a_ordenar]:
            filas[j], filas[j + 1] = filas[j + 1], filas[j]

with open('pacientes_ordenados.csv', mode='w', newline='', encoding='utf-8') as archivo_nuevo:
    escritor = csv.writer(archivo_nuevo)
    escritor.writerow(encabezado)
    escritor.writerows(filas)

print(" PRIMEROS 10 PACIENTES ORDENADOS POR APELLIDO")
for fila in filas[:10]:
    print(fila)

print("El archivo pacientes_ordenados.csv fue creado.")