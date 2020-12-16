#A List in a dictionary
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    'karen': ['JS'],
}

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        texto = 'are'
    else:
        texto = 'is'

    print(f"\n{name.title()}'s favorite language {texto}:")
    for language in languages:
        print(f"\t{language.title()}")

