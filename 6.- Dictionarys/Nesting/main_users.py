#Adictionary in a Dictionary
users = {
    'einstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
    'fmercurie':{
        'first': 'freddy',
        'last': 'mercucurie',
        'location': 'england',
    }
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    fullname = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFullname: {fullname.title()}")
    print(f"\tLocation: {location.title()}")
