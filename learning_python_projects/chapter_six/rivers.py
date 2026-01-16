rivers = {
    'missisippi': 'united states',
    'nile': 'egypt',
    'congo': 'uganda'
}

for river, country in rivers.items():
    print(f'The {river.title()} are located in the {country.title()}')

for river in rivers.keys():
    print(river.title())
#This worked without the f string since there was no other text

for country in rivers.values():
    print(f'{country.title()}')