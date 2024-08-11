"""
/*
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 */"""
 
def count_words(text):
     text_list = text.split()
     contador_palabras = {}

     # Contar las palabras
     for palabra in text_list:
          if palabra in contador_palabras:
               contador_palabras[palabra] += 1 #le suma 1 a la palabra
          else:
               contador_palabras[palabra] = 0 #como no existe la palabra, la cre y le pone el valor

     for palabra, cantidad in contador_palabras.items():
          print(f"La palabra '{palabra}' aparece {cantidad} veces repetida")
               
          
          
count_words("hola hola hola como como estas")