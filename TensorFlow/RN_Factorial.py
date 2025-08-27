import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 1. Preparación de Datos
n = np.arange(1, 11, dtype=np.float32).reshape(-1, 1)
fact = np.array([np.math.factorial(int(i)) for i in n.flatten()], dtype=np.float32).reshape(-1, 1)

# Normalizamos para estabilizar el entrenamiento
max_fact = np.max(fact)
fact_norm = fact / max_fact
print('Shapes -> n:', n.shape, '| fact_norm:', fact_norm.shape, '| max_fact:', float(max_fact))

# 2. Creación del Modelo
modelo = tf.keras.Sequential([
    tf.keras.layers.Dense(units=25, activation='relu', input_shape=[1]),
    tf.keras.layers.Dense(units=25, activation='relu'),
    tf.keras.layers.Dense(units=1)
])

# 3. Compilación del Modelo
modelo.compile(optimizer='adam', loss='mean_squared_error')

# 4. Entrenamiento del Modelo
print("Entrenando el modelo...")
historial = modelo.fit(n, fact_norm, epochs=500, verbose=0)
print("¡Entrenamiento completado!")

# 5. Visualización de la Pérdida
plt.xlabel('# Epoca')
plt.ylabel('Magnitud de Pérdida')
plt.plot(historial.history['loss'])
plt.show()

# 6. Predicción
print("\nPredicción para el factorial de 11:")
prediccion_norm = modelo.predict(np.array([[11.0]], dtype=np.float32))
prediccion = prediccion_norm * max_fact
print("Predicción (normalizada):", prediccion_norm[0][0])
print("Predicción (desnormalizada):", prediccion[0][0])
print("Valor real (11!):", np.math.factorial(11))
