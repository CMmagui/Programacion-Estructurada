import time

def suma_objetivos(lista, objetivo):
    n = len(lista)
    for i in range(n):
        for j in range(i + 1, n):
            if lista[i] + lista[j] == objetivo:
                return True 
    return False    

def medir_y_probar(funcion, lista, objetivo):
    "Función para medir el tiempo de ejecución de cualquier lista."
    inicio = time.perf_counter()
    resultado = funcion(lista, objetivo)
    fim = time.perf_counter()
    
    tiempo_total = fim - inicio
    print(f"Tiempo de ejecución:{tiempo_total:.6f} segundos")

if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6]
    lista1 = [i for i in range(1000)]
    lista2 = [i for i in range(2000)]
    lista3 = [i for i in range(4000)]
    lista4 = [i for i in range(8000)]

    objetivo = 9
    objetivo1 = 100
    objetivo2 = 200 
    objetivo3 = 400 
    objetivo4 = 800 

    print("--- Pruebas de rendimiento ---")
    medir_y_probar(suma_objetivos, lista, objetivo)
    medir_y_probar(suma_objetivos, lista1, objetivo1)
    medir_y_probar(suma_objetivos, lista2, objetivo2)
    medir_y_probar(suma_objetivos, lista3, objetivo3)
    medir_y_probar(suma_objetivos, lista4, objetivo4) 