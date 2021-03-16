"""
The main program should use functions from music_reports and display modules
"""

from music_reports import *
from display import *
from file_handling import *

def delete_album_by_artist_and_album_name(albums, artist, album_name):
    """
    Deletes album of given name by given artist from list and updates data file

    :param list albums: currently existing albums
    :param str artist: artist who recorded the album
    :param str album_name: name of album to be deleted

    :returns: updated albums' list
    :rtype: list
    """



def ask_for_input(message):
    return input(message)

albums = import_data()

def main():
    """
    Calls all interaction between user and program, handles program menu
    and user inputs. It should repeat displaying menu and asking for
    input until that moment.

    You should create new functions and call them from main whenever it can
    make the code cleaner
    """
    try:
        print_albums_list(get_albums_by_genre(albums,"rock"))
        #print_albums_list()

    except FileNotFoundError:
        print("File not found!")



if __name__ == '__main__':
    main()
