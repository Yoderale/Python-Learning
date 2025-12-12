buffet_foods = (
    'spaghetti', 'mac n cheese',
    'fried chicken', 'steak',
    'mashed potatoes'
    )
for food in (buffet_foods):
    print(f'The buffet offers: {food.title()}')
buffet_foods = (
    'ice cream', 'porridge', 'fried chicken',
    'steak', 'mashed potatoes'
    )
for food in tuple(buffet_foods):
    print(f'The buffet offers: {food.title()}')
#Not necessary to explicitly say this is a tuple