"""/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */"""
 
def fibonacci(n):
     if n == 0:
          print("el numero debe ser mayor a 0")
          return False
     elif n == 1:
          print(0)
          return 0
     else:
          num1 = 0
          num2 = 1    
          print(num1)
          print(num2)

          for _ in range(n-2):
               print(num1+num2)
               num1 , num2 = num2 , num1+num2
fibonacci(3)