def make_shirt(size, msg_printed = 'I love Python'):
    '''Display information about sise a msg of the t-shirt'''
    print(f"\nThe tshirt's size is: {size.upper()}")
    print(f"\nThe tshirt's message is: {msg_printed.title()}")


make_shirt('l')
make_shirt('m')
make_shirt(size = "s", msg_printed = "I am happy!!!")