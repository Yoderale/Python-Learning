'''
3-10. Every Function: Think of things you could store in a list. For example, you
could make a list of mountains, rivers, countries, cities, languages, or anything
else you’d like. Write a program that creates a list containing these items and
then uses each function introduced in this chapter at least once.
pop() - Removes the last item in the index
append() -  Inserts the an item to the end of a list
len() - counts the length of the list 
insert - insert item into a list at a specific point of the index
del - permanently deletes an item from a list
title() 
reverse() - Changes the list permanently
sorted() - Does not change the list, organizes in alphabetical 
sorted(reverse = True) - Does not change the list, reverse alphabetical order
sort - changes the list permanently and puts it in alphabetical order
Additional Mountains
----------------
Nanga Parbat
Annapurna I
Gasherbrum I
Broad Peak
Gasherbrum II
Shishapangma 
'''

mountains = ['kanchenjunga','everest', 'k2', 'Cho oyu', 'lhotse', 'makalu', 'dhaulagiri', 'manaslu']
print(f'{mountains[-1].title()}')
len(mountains)
print(f'This is how many mountains there are in the list: {len(mountains)}')

mountains.append('Nanga Parbat')
print(f'{mountains[-1].title()}')

mountains.append('annapurna i')
mountains.append('Gasherbrum I')
mountains.insert(0, 'Broad Peak')
print(f'{mountains}')

mountains.pop()
print(f'{mountains}')

del(mountains[-1])
print(f'{mountains}')

print(f'{sorted(mountains, reverse = True)}')
print(f'{sorted(mountains)}')

print(f'This is how many mountains there are in the list: {len(mountains)}')
print(mountains[0::])
mountains.reverse()
print(f'{mountains}')
mountains.sort()
print(f'{mountains}')