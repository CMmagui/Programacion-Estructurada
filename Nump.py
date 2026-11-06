# Ejercicio 1: Presion sistolica
import numpy as np
sistolica = np.array([118, 135, 142, 110, 128, 155, 121])

promedio = np.mean(sistolica)
desviacion = np.std(sistolica)

print("--- EJERCICIO 1 ---")
print(f"Promedio: {promedio:.2f}")
print(f"Desviación estándar: {desviacion:.2f}")

#----------------------------------------------------
mascara = sistolica >= 130
conteo = np.sum(mascara)
print(f"Lecturas >= 130 mmHg: {conteo}")

#----------------------------------------------------
posiciones = np.flatnonzero(mascara)
print(f"Posiciones: {posiciones}")


# Ejercicio 2: Glucosa en tres dias
glucosa = np.array([
    [ 95, 102,  99],
    [140, 155, 148],
    [ 88,  91,  85],
    [110, 118, 125]
])
promedio_pacientes = np.mean(glucosa, axis=1)
promedio_por_dias = np.mean(glucosa, axis=0)
dia_mas_alto = np.argmax(promedio_por_dias) + 1

posicion_plana = np.argmax(glucosa)
paciente_idx, dia_idx = np.unravel_index(posicion_plana, glucosa.shape)

print("--- EJERCICIO 2 ---")
print(f"Promedio por paciente:{promedio_pacientes}")
print(f"Promedio por día:{promedio_por_dias} (Día más alto: Día {dia_mas_alto})")
print(f"Máximo: Paciente{paciente_idx + 1}, Día {dia_idx + 1}")

# Ejercicio 3: Normalizacion min-max
datos = np.array([
    [36.5,  72,  95],
    [38.2, 104, 140],
    [37.0,  80,  88],
    [36.8,  65, 110],
    [39.1, 112, 125]
])
minimos = np.min(datos, axis=0)
maximos = np.max(datos, axis=0)

datos_escalados = (datos - minimos) / (maximos - minimos)
print("--- EJERCICIO 3 ---")
print("Datos Escalados (Rango [0, 1]):")
print(datos_escalados)

min_verificacion = np.min(datos_escalados, axis=0)
max_verificacion = np.max(datos_escalados, axis=0)

print(f"Mínimos por columna:{min_verificacion}")
print(f"Máximos por columna:{max_verificacion}")