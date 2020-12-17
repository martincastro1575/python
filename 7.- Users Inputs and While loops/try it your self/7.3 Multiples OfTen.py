prompt = "\nGive me a number for know if is multiples of ten?: "
number = int(input(prompt))

if number % 10 == 0:
    msg = f"{number} is Multiple of 10\n"
else:
    msg = f"{number} is not Multiple of 10\n"

print(msg)
