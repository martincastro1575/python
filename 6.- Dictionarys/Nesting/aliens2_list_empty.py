#A list of Dictionaries
#Make a list empty
aliens = []

#Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color':'green','points':5, 'speed':'slow'}
    aliens.append(new_alien)

#Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

#Show how many aliens have been created
print(f"Total numbers of aliens: {len(aliens)}")