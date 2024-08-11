"""
/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */"""

def invertidCadena(cadena):
     print("cadena original: ",cadena)
     print("cadena modificada: ",cadena[::-1])

invertidCadena("Hola mundo")