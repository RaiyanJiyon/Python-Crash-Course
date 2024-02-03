""" 8-8. User Albums: Start with your program from Exercise 8-7. Write a whileloop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop. """

# From 8.7 
def make_album(artist_name, album_title, tracks=None):
    album = {"artist": artist_name, "title": album_title}
    
    if tracks is not None:
        album["tracks"] = tracks

    return album

# Create three dictionaries representing different albums
album1 = make_album("Taylor Swift", "Folklore")
album2 = make_album("Kendrick Lamar", "DAMN")
album3 = make_album("Billie Eilish", "When We All Fall Asleep, Where Do We Go?", tracks=14)

# Print each return value to show that the dictionaries are storing the album information correctly
print(album1)
print(album2)
print(album3)

# User input loop
while True:
    print("Enter Artist name and Album name or Enter 'quit' for exit - ")
    
    # Capture user input for artist name
    artist_input = input("Artist: ")

    # Check if the user wants to quit
    if artist_input.lower() == 'quit':
        break
    
    # Capture user input for album title
    album_input = input("Album: ")

    # Call make_album with the user's input and print the resulting dictionary
    user_album = make_album(artist_input, album_input)
    print(user_album)
