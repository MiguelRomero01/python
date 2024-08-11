"""
/*
 * Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */"""
 
def capitalize_word(text):
     lettersDict = {
          'a': 'A', 
          'b': 'B', 
          'c': 'C', 
          'd': 'D', 
          'e': 'E', 
          'f': 'F', 
          'g': 'G', 
          'h': 'H', 
          'i': 'I', 
          'j': 'J', 
          'k': 'K', 
          'l': 'L', 
          'm': 'M', 
          'n': 'N', 
          'o': 'O', 
          'p': 'P', 
          'q': 'Q', 
          'r': 'R', 
          's': 'S', 
          't': 'T', 
          'u': 'U', 
          'v': 'V', 
          'w': 'W', 
          'x': 'X', 
          'y': 'Y',
     }
     wordCapitalized  =  ''
     
     for i in text:
          if i in lettersDict:
               wordCapitalized += lettersDict[i] + ''
          else:
               wordCapitalized += i + ''
          
     return wordCapitalized
     
print(capitalize_word("hola mundo?"))
          
