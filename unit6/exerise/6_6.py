favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python'
        }

friends = ['jen', 'phil']

for name in favorite_languages.keys():
    if name in friends:
        print("thank " + name.title())
    else:
        print("please join " + name.title())
        

