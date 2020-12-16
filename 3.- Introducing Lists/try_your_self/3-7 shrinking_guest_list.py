guests = ['margaret', 'simon', 'juana']

#new guests
guests.insert(0, 'maria')
guests.insert(2,'pedro')
guests.append('patricia')

print('\nGuest list to dinner:',f"\n\tGuest number one: {guests[0].title()}",
      f"\n\tGuest number two: {guests[1].title()}",
      f"\n\tGuest number three: {guests[2].title()}",
      f"\n\tGuest number four: {guests[3].title()}",
      f"\n\tGuest number five: {guests[4].title()}",
      f"\n\tGuest number six: {guests[5].title()}")

print("\nI'm so sorry my dears, The new table won't arrive in time for dinner",
    "So, I can invate only two people\n")
popped_guest = guests.pop()
print(f"\tSorry! {popped_guest.title()}, I cannot invite you")
popped_guest = guests.pop()
print(f"\tSorry! {popped_guest.title()}, I cannot invite you")
popped_guest = guests.pop()
print(f"\tSorry! {popped_guest.title()}, I cannot invite you")
popped_guest = guests.pop()
print(f"\tSorry! {popped_guest.title()}, I cannot invite you")

print(f"\nThis is the new guests list: {guests[0].title()}, {guests[1].title()}")

del guests[0]
del guests[0]

print(f"Empty Guest List {guests}")
