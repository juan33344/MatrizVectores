#identificar las palabras claves mas relivantes en un texto

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

mensaje = "el procesamiento de lenguaje natural es una disciplina fascinante."


# Tokenizar el texto
palabras = word_tokenize(mensaje)

# Filtrar las palabras vacías
stop_words = set(stopwords.words("spanish")) 
palabras_clave = [word for word in palabras if word.lower() not in stop_words]

print("Palabras clave:", palabras_clave) # Palabras clave: ['procesamiento', 'lenguaje', 'natural', 'disciplina', 'fascinante', '.']