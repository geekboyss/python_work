favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python'
        }

print("The following languages have been mentioned:")

# just value
for language in favorite_languages.values():
    print(language.title())

# use set
for language in set(favorite_languages.values()):
    print(language.title())
    
