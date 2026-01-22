'''
Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title.
Once you have that information, call make_album() with the user’s input and print the dictionary that’s created.
Be sure to include a quit value in the while loop.
'''
def make_album(name, title, num_songs = None):
    album = {
        'name': name,
        'title': title
        }
    if num_songs:
        album['num_songs'] = num_songs
    return album
    # originally this was converting the dictionary to an f stringp
    # added an if statement with a break to account for either input contains 'quit'

while True:
    print('Type quit at any time to exit the program')
    album_reponse = input(f"What is the artist's name? ")
    if album_reponse.lower() == 'quit':
        break
    title_response  = input(f"What is the title of the album? ")
    if title_response.lower() == 'quit':
        break
    album = make_album(album_reponse, title_response)
    print(album)
print('Thank you for your response!')



# while add_album_bool:
#     name = input(f"What is the artist's name?")
#     title = input(f"What is the title of the album? ") 
#     if name.lower() == 'quit' or title.lower() == 'quit':
#         break
#         add_album_bool = False
#         album = make_album(name, title)
# print(album)

# album = make_album('jimbo johnson', 'krieg')
# print(album)
# album = make_album('jack johnson', 'excalibur', num_songs = 1)
# print(album)
# album = make_album('jingleheimer johnson', 'knights day', num_songs = 8)
# print(album)