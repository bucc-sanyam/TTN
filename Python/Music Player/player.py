from collections import OrderedDict
from datetime import date
import pygame
import os
import sys

pygame.init()
pygame.mixer.init()
song_list = os.listdir('/home/ttn/Desktop/ttn/TTN/Python/Music Player/music/')
os.chdir("/home/ttn/Desktop/ttn/TTN/Python/Music Player/music/")
song_stopped = True

# Playing song options

def while_playing(song_stopped):
    '''To play a given song and perform various functions on it'''
    print("What do you wanna do next?\n"+
            "1. Play song.\n"+
            "2. Pause the song.\n"+
            "3. Stop the song.\n"+
            "4. Play next song.\n"+
            "5. Play previous song. \n"+
            "6. Add song to favourites.\n"+
            "7. Add song to a playlist.\n"+
            "8. Go back to main menu. \n")
    try:
        song_choice = int(input("\nEnter choice : "))
        if ((song_choice == 1) and (song_stopped == True)):
            play_song()
        elif ((song_choice == 1) and (song_stopped == False)):
            unpause_song()
        elif song_choice == 2:
            pause_song()
        elif song_choice == 3:
            stop_song()
        elif song_choice == 4:
            next_song()
        elif song_choice == 5:
            previous_song()
        elif song_choice == 6:
            add_to_fav(song_list[song_number])
        elif song_choice == 7:
            playlist_name = input("Enter the playlist name you want add song to : ")
            playlist_is_present = validate_playlist_name(playlist_name)
            if playlist_is_present:
                add_to_playlist(song_list[song_number], playlist_name)
            else:
                print("Try again with a valid playlist name.")
                while_playing(song_choice)
        elif song_choice == 8:
            song_stopped = False
            display_actions()
        else :
            print("No such options available.")
            while_playing(song_stopped)

    except SystemExit :
        sys.exit(0)

    except :
        print("Please enter a valid input.\n")
        while_playing(song_stopped)

def play_song():
    '''To play song'''
    global song_stopped
    if(song_stopped == True):
            pygame.mixer.music.load(song_list[song_number])
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                song_stopped=False
                while_playing(song_stopped)
    else :
            unpause_song()
def stop_song():
    '''To stop song'''
    global song_stopped
    pygame.mixer.music.stop()
    song_stopped = True
    while_playing(song_stopped)

def pause_song():
    '''To pause song'''
    global song_stopped
    pygame.mixer.music.pause()
    song_stopped=False
    while_playing(song_stopped)

def unpause_song():
    '''To resume song'''
    global song_stopped
    pygame.mixer.music.unpause()
    song_stopped=False
    while_playing(song_stopped)

def next_song():
    '''To play next song'''
    global song_number, song_stopped
    if song_number<(len(song_list)-1):
        song_number = song_number+1
    else:
        song_number = 0
    song_stopped = True
    play_song()

def previous_song():
    '''To play previous song'''
    global song_number, song_stopped
    if song_number<len(song_list) and song_number > 0:
        song_number = song_number-1
    else:
        song_number = len(song_list)-1
    song_stopped = True
    play_song()


## Actions performed


def perform_action(choice):
    '''Options for main menu'''
    
    if ( choice == 1 ):
        play_song()
        
        
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

    elif ( choice == 9 ):
        display_song_list(current_playlist_name, current_playlist)

    elif ( choice == 10 ):
        print("Thanks for using the player.")
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        sys.exit(0)


def add_songs():
    for song in song_list:
        playlists[current_playlist_name][song]=str(date.today())



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
    for key in playlists[current_playlist_name]:
        print("- "+str(key))
    display_actions()


def sort_songs_by_date():
    clone_playlist = playlists[current_playlist_name].copy()
    playlists[current_playlist_name].clear()
    clone_playlist = sorted(clone_playlist.items(), key = lambda kv:(kv[1], kv[0]))  
    for key in clone_playlist:
        print("- "+str(key))
    display_actions()

## Display 

def display_actions():
    '''Display main menu options'''
    print("\nChoose from following actions :"+
    "\n1. Play songs from current playlist. "+
    "\n2. Play songs on shuffle."+
    "\n3. Select other playlist."+
    "\n4. Add a new playlist."+
    "\n5. Remove a playlist."
    "\n6. Add a song to other playlist."+
    "\n7. Remove a song from current playlist."+
    "\n8. Sort songs in the current playlist."+
    "\n9. List the songs in playlist."+
    "\n10. Exit player.")
    try:
        choice = int(input("\nEnter choice : "))
        if 10 < choice <= 0:
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
    display_actions()

## Playlist features

def add_to_playlist(song_name, playlist_name):
    '''To add a song in a playlist'''
    song_available = validate(song_name, playlist_name)
    if (song_available):
        print("\nSong already present in playlist.\n")
    else:
        playlists[playlist_name][song_name] = str(date.today())
        print(f"{song_name} added to {playlist_name}.")
    display_actions()

def remove_from_playlist(song_name, playlist_name):
    '''To remove a song in a playlist'''
    song_available = validate(song_name, playlist_name)
    if (song_available):
        playlists[playlist_name].pop(song_name)
        print(f"{song_name} deleted from {playlist_name}.")
    else:
        print("\nSong not present in playlist.\n")
    display_actions()

def add_playlist(playlist_name):
    '''To directly add a playlist'''
    playlists[playlist_name]={}
    print("The updated playlists are : ")
    i=1
    for keys in playlists:
        print(str(i)+". "+keys)
        i=i+1
    display_actions()
    

def remove_playlist(playlist_name):
    '''To directly remove a playlist by name'''
    playlist_available = validate_playlist_name(playlist_name)
    if (playlist_available):
        playlists.pop(playlist_name)
        print(f"{playlist_name} removed.")
    else:
        print("\nPlaylist not present.\n")
    display_actions()

def add_new_playlist():
    '''To add a playlist while providing options'''
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
    '''To remove a playlist while providing options'''
    playlist_available = False
    for key in playlists:
        print("- "+key)
    while(playlist_available == False):
        playlist_selected = input("\nEnter the playlist name you want to remove : ")
        playlist_available = validate_playlist_name(playlist_selected)
        if(playlist_available):          
            remove_playlist(playlist_selected)

def add_song_to_playlist():
    '''To add songs to a playlist while providing options'''
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
    '''To remove song from a playlist while providing options'''
    song_available = playlist_available =False
    print("\nEnter the song and playlist name.\n")
    while(song_available):
        song_name = input("Song : ")
        song_available = validate_song_name(song_name)
    while(playlist_available):
        playlist_name = input("Playlist : ")
        playlist_available = validate_playlist_name(playlist_name)
    remove_from_playlist(song_name, playlist_name)


def select_other_playlist():
    '''To select some other playlist'''
    global current_playlist_name, current_playlist
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


def add_to_fav(song_name):
    '''To add songs in favourite playlist'''
    add_to_playlist(song_name, "Favourite")

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
        print("No such playlist exist.\n")
        return False


song_number = 0
print("\n\nWelcome to TTN Music Player\n")
playlists = OrderedDict()
playlists["Default"] = {}
playlists["Favourite"] = {}
playlists["Bucc"] = {}
current_playlist_name = "Default"
add_songs()

current_playlist = playlists[current_playlist_name]
display_song_list(current_playlist_name, current_playlist)
display_actions()
       
