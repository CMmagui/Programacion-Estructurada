import pandas as pd

# Ejercicio 4: Carga y explora
df = pd.read_csv("pacientes - pacientes.csv")

print("--- EJERCICIO 4 ---")
pacientes, columnas = df.shape
print(f"Existen {pacientes} pacientes y hay {columnas} columnas.")

faltantes = df.isna().sum()
faltantes_filtrados = faltantes[faltantes > 0]
print("Columnas con valores faltantes:")
print(faltantes_filtrados)

print("Tipo de dato por columna:")
print(df.dtypes)


# Ejercicio 5: Alerta clinica
print("--- EJERCICIO 5 ---") 
alerta = df[(df["temp_c"] >= 38) & (df["fc_lpm"] > 100)]

print(f"Existen {len(alerta)} pacientes en alerta:")
print(alerta[["id", "temp_c", "fc_lpm", "servicio" ]])

print("Están en los siguientes servicios:")
print(alerta ['servicio'].value_counts())   


# Ejercicio 6: IMC y clasificacion 
print("--- EJERCICIO 6 ---")
df["imc"] = df["peso_kg"] / (df["estatura_m"] ** 2)

bins = [0, 18.5, 25, 30, 100]
labels = ["Bajo peso", "Normal", "Sobrepeso", "Obesidad"]
df["clasificacion_imc"] = pd.cut(df["imc"], bins=bins, labels=labels, right=False)

print("Conteo por su categoría:")
print(df["clasificacion_imc"].value_counts())

sin_imc = df["imc"].isna().sum()
print(f"Pacientes sin IMC: {sin_imc} Faltaron algunos datos de peso_kg")


# Ejercicio 7: Resumen por servicio
print("--- EJERCICIO 7 ---")    
resumen = (
    df.groupby("servicio")
    .agg(
        num_pacientes=("id", "count"),
        temp_promedio=("temp_c", "mean"),
        fc_promedio=("fc_lpm", "mean")
    )
    .round(1)
    .sort_values(by="fc_promedio", ascending=False)
)

print(resumen)