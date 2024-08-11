"""/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */"""
 
def even():
     for num in range(1,100+1):
          count = 0
          for i in range(1,num+1):
               if num % i == 0:
                    count += 1
          if count == 2:
                print(num)
                
even()
          
          