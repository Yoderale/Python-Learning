'''
3-8. Seeing the World: Think of at least five places in the world you’d like to visit.

• Use sort() to change your list so it’s stored in alphabetical order. Print the
list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse-alphabetical order.
Print the list to show that its order has changed.'''
#• Store the locations in a list. Make sure the list is not in alphabetical order.

vacation_destination = ['greece', 'spain', 'atlantis', 'cotswalds', 'puerto rico']
#  Print your list in its original order. Don’t worry about printing the list neatly;
#  just print it as a raw Python list.
print(vacation_destination)

# Use sorted() to print your list in alphabetical order without modifying the actual list.
print(sorted(vacation_destination))

# Show that your list is still in its original order by printing it.
print(vacation_destination)

# Use sorted() to print your list in reverse-alphabetical order without changing
# the order of the original list.
print(sort(vacation_destination, reverse = True))

# Show that your list is still in its original order by printing it again.
print(vacation_destination)

'''
Use reverse() to change the order of your list. Print the list to show that its
order has changed. '''
print(vacation_destination.reverse())
print(vacation_destination)
'''Use reverse() to change the order of your list again. Print the list to show
it’s back to its original order.'''
print(vacation_destination.reverse())
print(vacation_destination)