def make_shirt(size, msg_printed):
    '''Display information about sise a msg of the t-shirt'''
    print(f"\nThe tshirt's size is: {size.upper()}")
    print(f"\nThe tshirt's message is: {msg_printed.title()}")

make_shirt('l', 'I love of live')
make_shirt(msg_printed = 'I am happy!!!', size = 'm')