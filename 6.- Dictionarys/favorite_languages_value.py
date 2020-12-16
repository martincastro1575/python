favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'erin': 'c#'
}

print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(f"\t{language.title()}")
