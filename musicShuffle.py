import random

my_songs = {'Real Shit': 1, 'Juice Wrld DID': 2, 'All Dz Chainz': 3,
            'Moncler Year': 4, 'Astronauts': 5, '735': 6, 'Choppa': 7, 'Awful Times': 8}  # dictionary of songs

# create a random number generator out of the values in the dictionary

# extracts all the values from song dictionary and places them in val_list
val_list = list(my_songs.values())

# creates a list of all the keys in the dictionary
key_list = list(my_songs.keys())

# the used songs, that won't be generated randomly
used_songs = []


def unload():
    used_songs.clear()

def shuffledList():

    songOrder = [] # place holder

    for x in key_list: # loop through dictionary key list to put in place holder
        songOrder.append(x)

    random.shuffle(songOrder) # randomize the list

    # print(songOrder) 

def next_song1():

    t = 0

    while t == 0:
        # selects random number from my_list
        song_selection = (random.randrange(len(val_list)) + 1)

        if song_selection in used_songs:
            continue
        else:
            # takes the song number and uses it as an index for val_list

            # this is a test
            # print(f"This is the random song selection {song_selection}")

            # print(val_list)  # this is a test

            # print(key_list)  # this is a test '''

            song = val_list.index(song_selection)

            # this is a test
            # print(f"This is the value that corrisponds with the song selection {song}")

            # stores all the selected songs
            used_songs.append(song_selection)

            print("-----------------------------------------------")
            print(f'Now Playing...  {key_list[song]}')
            print("-----------------------------------------------")
            print("")

            t = 1

    # I can figure out how to remove the items in used songs once it hits it's max, and allow the user to repeat

    if len(used_songs) == len(my_songs):
        print("")
        print("-----------------------------------------------")
        print("There are no more songs in the rotation...")
        print("-----------------------------------------------")
        print("")
        unload()

def previous_song1():

    # index = song_selection.index()

    previous_song = used_songs[-2]

    values = val_list.index(previous_song)

    print("-----------------------------------------------")
    print(f"Now Playing... {key_list[values]}")
    print("-----------------------------------------------")

    # works but we now need to remove the value from used_songs, so when we press previous again, it does the next song in the list


num = 0
while num == 0:
    print("Music Player - Main Menu")
    print(" ")
    print("1 - Next Song, 2 - Previous Song, 3 - Exit Program")
    print(" ")

    prompt = int(input(f"Please select an option: "))
    print("")

    if prompt == 1:
        
        continue
    elif prompt == 2:
        
        continue
    elif prompt == 3:
        num = 1
        print("Closing Music Player...")
    else:
        print("Please read instructions again.")

# testing orderedList function



# Mar 3rd 1:47:38 AM
# Next steps are to check if song_selection's next generated number equals a value in the used_songs list
# If it matches with a value, it should run again. It keeps running till it finds a new value


# Mar 3rd 4:24:54 PM

# Figured out how to not use repeated values

# Next steps is to stop the loop and prompt the users to exit or figure out a way to dish the used_songs items, and allow the user to continue pressing next song, for a new rotation.

# Mar 5th 10:56:09 PM

# We want to end the loop after it is completed, and then empty out used_songs, so the loop can run again

# Check to see how to rewind to the last song

# General Idea: Get the last updated item in used songs, and get the corrisponding song that goes with it.

# Check out red dots to see the tests
