foods = ['pizza', 'hotdog', 'ice cream', 'steack']

friend_foods = foods[:] #de esta manera copio una lista a otra usando [:]

print(f"\nMy favorite foods are: {foods}")
print(f"Friend's favorite foods are: {friend_foods}")

#Agregando nuevas comidas a cada lista
foods.append('canoli')
friend_foods.append('pasta')

print(f"\nMy favorite foods are: ")
for food in foods:
    print(f"\t{food}")

print(f"\nFriend's favorite foods are:")
for food in friend_foods:
    print(f"\t{food}")