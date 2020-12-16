guests = ['margaret', 'simon', 'juana']

print('\t\nGuest list to dinner:',f"\n\tGuest number one: {guests[0].title()}",
      f"\n\tGuest number two: {guests[1].title()}",
      f"\n\tGuest number three: {guests[2].title()}")

print("I've got had news for you, my dears!!!", 
        "I've found a big table for dinner. So", 
        "I've invated three special people more.")

guests.insert(0, 'maria')
guests.insert(2,'pedro')
guests.append('patricia')



print('\nUpdate Guest list to dinner:',f"\n\tGuest number one: {guests[0].title()}",
      f"\n\tGuest number two: {guests[1].title()}",
      f"\n\tGuest number three: {guests[2].title()}",
      f"\n\tGuest number four: {guests[3].title()}",
      f"\n\tGuest number five: {guests[4].title()}",
      f"\n\tGuest number six: {guests[5].title()}")

