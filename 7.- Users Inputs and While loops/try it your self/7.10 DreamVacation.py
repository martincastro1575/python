dream_vacations = {}

active = True

while active:
    name = input("\nWhat's your name? ")
    place = input("\nIf you could visit one place, Where would you go? ")

    dream_vacations[name] = place

    resp = input("\nWould you like to continue with the poll?, (y/n) ")

    if resp.lower() == 'n':
        active = False
    
print("\n--- Poll Results ---")
for name, place in dream_vacations.items():
    print(f"{name.title()} will like to go {place.title()}" )
print("\n")
    