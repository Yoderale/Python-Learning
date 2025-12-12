#I LOVE PIZZA PIE
pizzas = ['meat lovers', 'pepperoni', 'hawaiian']
for pizza in pizzas:
	print(f'I like {pizza.title()} pizza! Its my favorite!')
print("It's better than life itself!")
friends_pizzas = pizzas[:]
print(friends_pizzas)

pizzas.append('margherita')
friends_pizzas.append('cheese only')
for pizza in pizzas:  
 	print(f"My favorite pizzas are: {pizza}")
for friends_pizza in friends_pizzas:  
	print(f"My friends favorite pizzas are: {friends_pizza}")