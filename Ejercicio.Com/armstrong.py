"""/*
 * Escribe una función que calcule si un número dado es un número de Armstrong
 * (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información
 * al respecto.
 */"""
 
def armstrongNumber(Number):
     numberList = list(str(Number))
     result = 0
     
     for digit in numberList:
        result += int(digit) ** len(numberList)

     return list(str(result)) == numberList

print(armstrongNumber(153))