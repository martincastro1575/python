first_name = 'MarTin'
last_name = 'Castro'
message = 'Hello {} {}, would you like to learn some Python today?'.format(first_name, last_name)
name_famous_person = '"Albert Eisten"'
complement = 'once said'
quote = 'A person who never made a mistake never tried anything new.'
full_quote = f'\n{complement.title()}\n {quote.title()} \n\t\t\t\t\t\t{name_famous_person.upper()}'
print(message)
print(first_name.upper())
print(first_name.lower())
print(first_name.title())
print('{} {}, {} '.format(name_famous_person, complement, quote))
print(full_quote)