"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */"""
 
def anagrama(word1,word2):
     return sorted(word1.lower()) == sorted(word2.lower()) #ordena las palabras y si es igual retorna true o false
          
print(anagrama("ballena","llenaba"))