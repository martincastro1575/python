def build_profile(first, last, **user_info):
    """ Build a dictionary containing everything we know about user. """
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()

    return user_info

user_profile = build_profile('martin',
                             'jose',
                            location= 'BA',
                            age= 45,
                            grade= 'computer engineer',
                            sexo= 'masculino')


print(user_profile)