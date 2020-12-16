age = 65
stage_of_life = ['baby', 'toddler', 'kid','teenager','adult','elder']

if age < 2:
    index= 0
elif age >= 2 and age <4:
    index = 1
elif age >=4 and age < 13:
    index = 2
elif age >= 13 and age < 20:
    index = 3
elif age >= 20 and age < 65:
    index = 4
else:
    index = 5

print(f"\nThe person is {age} years old, the person is {stage_of_life[index]}.")