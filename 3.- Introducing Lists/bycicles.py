bycicles = ['trek','cannondale','readline','specialized',]
print(bycicles)

#Accesing Elements in a list
msg = 'one element'
element = bycicles[0].upper()
print('{}: {}'.format(msg.title(), element))

#Accesing the last element in list
last_element = bycicles[-1].title()
last_element_second = bycicles[-2].upper()
print(last_element)
print(last_element_second)

#Using inviduals value from a list
message = f'My first bycicle was a: {bycicles[0].title()}'
print(message)