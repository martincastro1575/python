guests = ['margaret', 'simon', 'carolina']


print('\tGuest list to dinner:',f"\n\tGuest number one: {guests[0].title()}",
      f"\n\tGuest number two: {guests[1].title()}",
      f"\n\tGuest number three: {guests[2].title()}")

print(f"\nGuest list doesn't come to dinner: \n\t\t\t{guests[2].title()}")

'replaced carolina by juana'
guests[2]='juana'
guest_number = len(guests)
print('\t\nUpdate Guest list to dinner:',f"\n\tGuest number one: {guests[0].title()}",
      f"\n\tGuest number two: {guests[1].title()}",
      f"\n\tGuest number three: {guests[2].title()}",f"\n\t\t\tTotal Guests: {guest_number}")



