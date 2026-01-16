pets = []

pet = {
    'name': 'max',
    'type': 'dog',
    'owner': 'alex'}
pets.append(pet)

pet = {
    'name': 'bella',
    'type': 'cat',
    'owner': 'sarah'
}
pets.append(pet)

pet = {
    'name': 'cooper',
    'type': 'dog',
    'owner': 'michael'
}
pets.append(pet)

pet = {
    'name': 'luna',
    'type': 'rabbit',
    'owner': 'jessica'
}
pets.append(pet)

pet = {
    'name': 'speedy',
    'type': 'turtle',
    'owner': 'daniel'
}
pets.append(pet)

pet = {
    'name': 'daisy',
    'type': 'bird',
    'owner': 'emily'
}
pets.append(pet)

pet = {
    'name': 'charlie',
    'type': 'hamster',
    'owner': 'ryan'
}
pets.append(pet)

for pet in pets: 
    print(f'The pet name is: {pet['name'].title()}, and it is a {pet['type'].title()}, and the owner is named: {pet['owner'].title()}.')

for pet in pets:
    print(f'{pet['name']}, here is what I know about them:\n')
    for key, value in pet.items():
        print(f'{key}, {value}')