#vamos a dividir un texto en palabras o frases 
import nltk 
nltk.download('all') #descargamos el paquete punkt
from nltk.tokenize import word_tokenize, sent_tokenize  

mensaje = "Hola, ¿cómo estás? Espero que estés teniendo un buen día. ¡Nos vemos pronto!"

palabras = word_tokenize(mensaje.rstrip())
oraciones = sent_tokenize(mensaje)

print("Palabras:", palabras)
print("Oraciones:", oraciones)