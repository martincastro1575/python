def print_send_messages(mesagges, sent_messages):
    '''Print each message'''
    while mesagges:
        current_message = mesagges.pop()
        print(f"Text message: {current_message}")
        sent_messages.append(current_message)

def print_sent_messages(sent_messages):
    print("\nList of sent messages: ")
    for sent_message in sent_messages:
        print(sent_message)
         

messages_text = ['hola, como estas?', 'Bienvenido a nuestro sistema', 'Adios, fue grato conocerte!']
sent_messages = []

#Estoy pasando como primer argumento una copia de la lista
#de mensajes
print_send_messages(messages_text[:], sent_messages)
print_sent_messages(sent_messages)