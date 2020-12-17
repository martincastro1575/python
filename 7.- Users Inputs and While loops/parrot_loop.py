prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter quit to end the program: "

activate = True

while activate:
    msg = input(prompt)
    
    if msg.lower() == 'quit':
        activate = False
    else:
        print(msg)

    