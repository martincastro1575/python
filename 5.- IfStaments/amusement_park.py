age = 65

if (age < 4):
    price = 0
elif (age < 18):
    price = 24
elif (age < 65):
    price = 40
elif (age >= 65):
    price = 20

print(f"\nYou are {age} years old, your admission cost is {price} $.\n")