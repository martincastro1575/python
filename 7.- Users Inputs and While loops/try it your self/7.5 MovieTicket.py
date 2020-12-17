prompt = "\nPlease tell me; how old are you?"
prompt += "\nOr Enter 'q' to exit: "

while True:
    age = input(prompt)
    msg = ''
    if age.isdigit() == True:
        age = int(age)
        if age < 3:
            msg = "Your ticket is (free)"
        elif age >= 3 and age <= 12:
            msg = "Your have pay (10 US$)"
        elif age > 12:
            msg = "You have pay (15 US$)"
        
        print(f"\n{msg}")

    elif age.lower() == 'q':
        break

