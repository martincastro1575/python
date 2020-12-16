#Imprime los numeros del 1 hasta el 1 millon
#Usando list comprehension
numbers = [value for value in range(1,1000001)]

print(f"El menor numero del 1 al 1.000.000 es: {min(numbers)}")
print(f"El mayor numero del 1 al 1.000.000 es: {max(numbers)}")
print(f"Sumando los numero del 1 al 1.000.000 es: {sum(numbers)}")