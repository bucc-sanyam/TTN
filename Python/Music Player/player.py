from collections import OrderedDict
from datetime import date


## Actions performed

def perform_action(choice):
    
    if ( choice == 1 ):
        normal_play()

    elif ( choice == 2 ):
        shuffle_play()
    
    elif ( choice == 3 ):  
        select_other_playlist()

    elif ( choice == 4 ):
        add_new_playlist()

    elif ( choice == 5 ):  
        remove_a_playlist()

    elif ( choice == 6 ):
        add_song_to_playlist()

    elif ( choice == 7 ):
        remove_song_from_playlist()

    elif ( choice == 8 ):
        sort_songs()

def select_other_playlist():
    playlist_available = False
    print("\nAvailable playlists are :")
    index = 1
    for playlist_name in playlists:
        print(str(index)+". "+playlist_name)
        index+=1
    while(playlist_available == False):
        playlist_selected = input("\nEnter choice : ")
        playlist_available = validate_playlist_name(playlist_selected)
        if(playlist_available):
            current_playlist_name=playlist_selected
            current_playlist = playlists[current_playlist_name]
            print(f"{current_playlist_name} selected.")
            break        

def add_new_playlist():
    playlist_available = False
    while(playlist_available == False):
        playlist_selected = input("\nEnter the playlist name you want to add : ")
        playlist_available = validate_playlist_name(playlist_selected)
        if(playlist_available):          
            print("Playlist already present.")
            break
        else:
            add_playlist(playlist_selected)
            break

def remove_a_playlist():
    playlist_available = False
    while(playlist_available == False):
        playlist_selected = input("\nEnter the playlist name you want to remove : ")
        playlist_available = validate_playlist_name(playlist_selected)
        if(playlist_available):          
            remove_playlist(playlist_selected)

def add_song_to_playlist():
    song_available = playlist_available =False
    print("\nEnter the song and playlist name.\n")
    while(song_available == False):
        song_name = input("Song : ")
        song_available = validate_song_name(song_name)
    while(playlist_available == False):
        playlist_name = input("Playlist : ")
        playlist_available = validate_playlist_name(playlist_name)
    add_to_playlist(song_name, playlist_name)

def remove_song_from_playlist():
    song_available = playlist_available =False
    print("\nEnter the song and playlist name.\n")
    while(song_available):
        song_name = input("Song : ")
        song_available = validate_song_name(song_name)
    while(playlist_available):
        playlist_name = input("Playlist : ")
        playlist_available = validate_playlist_name(playlist_name)
    remove_from_playlist(song_name, playlist_name)



##  Song play features

def play_song():
    pass


def stop_song():
    pass


def next_song():
    pass


def shuffle_play():
    pass


def normal_play():
    pass


## Sort


def sort_songs():
    print("\nSelect the sort you want :"+
        "\n1. Sort songs by name."+
        "\n2. Sort songs by date.")
    while(True):
        try:
            sort_choice = int(input("\nEnter choice : "))
            if( sort_choice == 1):
                sort_songs_by_name()
                break
            elif( sort_choice == 2):
                sort_songs_by_date()
                break
            else:
                raise Exception("Invalid Choice")
        except:
            print("Please enter a valid input.")

def sort_songs_by_name():
    clone_playlist = playlists[current_playlist_name].copy()
    playlists[current_playlist_name].clear()
    key_list = [key for key in clone_playlist]
    key_list.sort()
    for key in key_list:
        playlists[current_playlist_name][key] = clone_playlist[key]
    print(playlists[current_playlist_name])


def sort_songs_by_date():
    pass


## Display 

def display_actions():
    print("\nChoose from following actions :"+
    "\n1. Play songs from current playlist. "+
    "\n2. Play songs on shuffle."+
    "\n3. Select other playlist."+
    "\n4. Add a new playlist."+
    "\n5. Remove a playlist."
    "\n6. Add a song to other playlist."+
    "\n7. Remove a song from current playlist."+
    "\n8. Sort songs in the current playlist." )
    try:
        choice = int(input("\nEnter choice : "))
        if (choice > 8):
            raise Exception("Invalid Choice.")
    except:
        print("Please enter a valid choice.")
        display_actions()
    perform_action(choice)

def display_song_list(current_playlist_name, current_playlist):
    print(f"Currently the songs available in {current_playlist_name} playlist are : ")
    index=1
    for key in playlists[current_playlist_name]:
        print(str(index)+". "+key)
        index+=1

## Playlist features

def add_to_playlist(song_name, playlist_name):
    song_available = validate(song_name, playlist_name)
    if (song_available):
        print("\nSong already present in playlist.\n")
    else:
        playlists[playlist_name][song_name] = str(date.today())
        print(f"{song_name} added to {playlist_name}.")

def remove_from_playlist(song_name, playlist_name):
    song_available = validate(song_name, playlist_name)
    if (song_available):
        playlists[playlist_name].pop(song_name)
        print(f"{song_name} deleted from {playlist_name}.")
    else:
        print("\nSong not present in playlist.\n")

def add_playlist(playlist_name):
    playlists[playlist_name]={}
    print(playlists)

def remove_playlist(playlist_name):
    playlist_available = validate_playlist_name(playlist_name)
    if (playlist_available):
        playlists.pop(playlist_name)
        print(f"{playlist_name} removed.")
    else:
        print("\nPlaylist not present.\n")

## Validation

def validate(song_name, playlist_name):
    song_available = False 
    if song_name in playlists[playlist_name]:
            song_available = True
    if(song_available):
        return True #Song present in playlist
    else:
        return False #Song not present in playlist

   
def validate_song_name(song_name):
    song_available = False 
    if song_name in playlists[current_playlist_name]:
            song_available = True
    if(song_available):
        return True
    else:
        print("No such song present.\n")
        return False


def validate_playlist_name(playlist_name):
    playlist_available = False 
    if playlist_name in playlists:
            playlist_available = True
    if(playlist_available):
            return True
    else:
        print("No such playlist present.\n")
        return False



print("\n\nWelcome to TTN Music Player\n")
playlists = OrderedDict()
playlists["Default"] = {"Chop Suey": "21/02/2019", "Bohemian Rhapsody": "25/02/2019"}
playlists["Favourite"] = {}
playlists["Bucc"] = {}
current_playlist_name = "Default"
current_playlist = playlists[current_playlist_name]
display_song_list(current_playlist_name, current_playlist)
display_actions()
