#If the number is multiple of 3, it will print fizz. If the number is multiple of 5, it will print buzz. else if the number is multiple of 3 and 5, it will print fizzbuzz
def fizzBuzz (rangeUser):
     for i in range(1,rangeUser+1):
          if i % 3 == 0 and i % 5 == 0:
               print("fizzBuzz")
          elif i % 3 == 0:
               print("fizz")
          elif i % 5 == 0:
               print("buzz")
          else:
               print(i)
fizzBuzz(15)
