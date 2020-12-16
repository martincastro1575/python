prompt = "\nHow many people are in the dinner group?: "
qty_people = int(input(prompt))

if qty_people > 8:
    msg = "\nYou'll have to wait for a table."
else:
    msg = "\nYours table is ready."

print(msg)