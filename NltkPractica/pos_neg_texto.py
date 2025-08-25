# determinar si un texto tiene connotacion positiva o negativa

from nltk.sentiment import SentimentIntensityAnalyzer

mensaje = "Exito amigo NO me gusta para nada su algoritmo ."

# Crear un analizador de sentimientos
sia = SentimentIntensityAnalyzer()

# Analizar el sentimiento del mensaje
sentimiento = sia.polarity_scores(mensaje)

print("Análisis de Sentimiento:", sentimiento)