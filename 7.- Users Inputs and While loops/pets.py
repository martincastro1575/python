pets = ['cat', 'dog', 'tiger', 'mokey', 'goldfish','cat', 'rabbit','dog']

print(f"Original list: {pets} ")

while 'cat' in pets:
    pets.remove('cat')

print(f"List after removing 'cat': {pets}")