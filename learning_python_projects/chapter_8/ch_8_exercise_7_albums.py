"""
Write a function called make_album() that builds a dictionary describing a music album.
The function should take in an artist name and an album title, and it should return a 
dictionary containing these two pieces of information. Use the function to make three dictionaries 
representing different albums. Print each return value to show that the dictionaries are 
storing the album information correctly. 
Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album.
If the calling line includes a value for the number of songs, add that value to the album’s dictionary. 
Make at least one new function call that includes the number of songs on an album.
"""
def make_album(name, title, num_songs = None):
    album = {
        'name': name,
        'title': title
        }
    if num_songs:
        album = f"{name} {title}: {num_songs}" 
    else:
        album = f"{name} {title}"
    return album.title()
 
album = make_album('jimbo johnson', 'krieg')
print(album)
album = make_album('jack johnson', 'excalibur', num_songs = 1)
print(album)
album = make_album('jingleheimer johnson', 'knights day', num_songs = 8)
print(album)