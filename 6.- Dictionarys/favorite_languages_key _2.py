favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'erine': 'C#',
}

friends = ['phil', 'sarah']

if 'erin' not in favorite_languages:
    print("\nErin! please take our poll...\n")

for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name]
        print(f"\t{name.title()}, I see you love {language}!")