# 1st Methode Print The Table.
# Multiplication table Print in Python.

from time import sleep
  
number = input('Enter Your Table : ')
multiplier = input('How many Times Calculat? : ')
  
# printing the starting statement 
print(number,'calculation',multiplier, 'total')
  
# checking the type of variables
print(type(number), type(multiplier))
  
# lets convert them to integers
number =int (number)
multiplier =int (multiplier)
  
# check the type again
print(type(number),type(multiplier))
  
# table calculation
val = 1
  
while True:
    
  print(number,"X", val, "=", number * val)
    
# lets break the loop
  if val == multiplier:
   break
  
# increament the value
  val = val + 1    
  sleep(1)
  