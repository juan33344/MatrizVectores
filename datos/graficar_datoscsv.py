import pandas as pd
import matplotlib.pyplot as plt

df_ingresantes = pd.read_csv('datos/datos_ingresantes.csv', sep=';',encoding='utf-8')

#Agrupar por escuelas profesionales y obtener el maximo puntaje
puntaje_carrera = df_ingresantes.groupby('ESCUELA_PROFESIONAL')['PUNTAJE'].max()

# Ordenar los valores de mayor a menor
datos = puntaje_carrera.sort_values(ascending=False).reset_index().head(10)

# Crear el gráfico de barras
# print(datos)
plt.figure(figsize=(20, 12))
plt.bar(datos['ESCUELA_PROFESIONAL'], datos['PUNTAJE'],color='skyblue')

# Etiquetas y Titulo
plt.xlabel('Escuela ProfesionalL')
plt.ylabel('Puntaje')
plt.title('Puntaje por Escuela Profesional MAXIMO')

# Rotar las etiquetas del eje x para que sean legibles
plt.xticks(fontsize=6,rotation=45,ha='right')

# Mostrar el gráfico
plt.tight_layout()
plt.show()