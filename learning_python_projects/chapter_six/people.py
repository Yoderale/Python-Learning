people = []


person = {
    'age': 80,
    'first_name': 'chris',
    'last_name': 'crinkler',
    'location': 'north pole'
}
people.append(person)

person = {
    'age': 31,
    'first_name': 'alex',
    'last_name': 'yoder',
    'location': 'houston'
}
people.append(person)

person = {
    'age': 31,
    'first_name': 'nicholas',
    'last_name': 'kringle',
    'location': 'south pole'
}
people.append(person)

for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    location = person['location']

    print(f'{name} lives in, {location}, and is {age} years old!')