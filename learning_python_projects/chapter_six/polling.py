favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'john': '',
    'jacob': '',
    'jingleheimer': '',
    'buddy': ''
}

for name, language in favorite_languages.items(): 
    if language == '':
        print(f'{name.title()}, please take our poll!')
    else: 
        print(f'{language} is your favorite language, {name.title()}')
print(len(favorite_languages.keys()))