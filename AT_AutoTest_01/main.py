def add(a, b):
   return a + b

def subtract(a, b):
   return a - b

def multiply(a, b):
   return a * b

def divide(a, b):
   if b == 0:
       raise ValueError('Cannot divide by zero')
   return a / b

def check(number):
   return number % 2 == 0

def divide_zero(a, b):
   if b == 0:
       raise ValueError('На ноль делить нельзя')
   return a/b

def modulo(a, b):
   if b == 0:
      raise ValueError("Остаток от деления на ноль невозможен")
   return a % b
