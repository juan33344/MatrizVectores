#Asignar una etiqueta gramatical a cada palbra
from nltk import pos_tag 
from nltk.tokenize import word_tokenize

mensaje = "NLTK es una librería increible para el PLN."

# Tokenizar el texto
palabras = word_tokenize(mensaje)

# Etiquetar las palabras
etiquetas = pos_tag(palabras)

print("Etiquetas gramaticales:", etiquetas)