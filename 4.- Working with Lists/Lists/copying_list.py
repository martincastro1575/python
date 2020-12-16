foods = ['pizza', 'hotdog', 'ice cream', 'steack']

friend_foods = foods[:] #de esta manera copio una lista a otra usando [:]

print(f"My favorite foods are: {foods}")
print(f"Friend's favorite foods are: {friend_foods}")

#Agregando nuevas comidas a cada lista
foods.append('canoli')
friend_foods.append('pasta')
print("Add new foods")
print(f"My favorite foods are: {foods}")
print(f"Friend's favorite foods are: {friend_foods}")