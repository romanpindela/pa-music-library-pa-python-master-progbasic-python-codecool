from file_handling import *

artist_col = 0
album_col = 1
year_col = 2
genre_col = 3
length_col = 4


def get_albums_by_genre(albums, genre):
    """
    Get albums by genre

    :param list albums: albums' data
    :param str genre: genre to filter by

    :returns: all albums of given genre
    :rtype: list
    """

    genres = set(album[genre_col] for album in albums)
    if genre in genres:

        genre_albums = []

        for album in albums:
            if album[genre_col] == genre:
                genre_albums.append(album)

        return genre_albums
    else:
        raise ValueError("Wrong genre")



def get_genre_stats(albums):
    """
    Get albums' statistics showing how many albums are in each genre
    Example: { 'pop': 2, 'hard rock': 3, 'folk': 20, 'rock': 42 }

    :param list albums: albums' data
    :returns: genre stats
    :rtype: dict
    """


    genre_stats = {}
    for album in albums:
        if album[genre_col] in genre_stats:
            genre_stats[album[genre_col]] = genre_stats[album[genre_col]] + 1
        else:
            genre_stats[album[genre_col]] = 1


    return genre_stats


def get_longest_album(albums):
    """
    Get album with biggest value in length field.
    If there are more than one such album return the first (by original lists' order)

    :param list albums: albums' data
    :returns: longest album
    :rtype: list
    """
    longest_album = albums[0]
    for album in albums:
        if to_time(album[length_col]) > to_time(longest_album[length_col]):
            longest_album = album

    return longest_album



def get_last_oldest(albums):
    """
    Get last album with earliest release year.
    If there is more than one album with earliest release year return the last
    one of them (by original list's order)

    :param list albums: albums' data
    :returns: last oldest album
    :rtype: list
    """
    oldest_album = albums[0]
    for album in albums:
        if int(album[year_col]) <= int(oldest_album[year_col]):
            oldest_album = album

    return oldest_album


def get_last_oldest_of_genre(albums, genre) -> list:
    """
    Get last album with earliest release year in given genre

    :param list albums: albums' data
    :param str genre: genre to filter albums by
    :returns: last oldest album in genre
    :rtype: list
    """

    genre_albums = []
    for album in albums:
        if album[genre_col] == genre:
            genre_albums.append(album)

    return get_last_oldest(genre_albums)


def to_time(album_length: str):
    """
    converts time in format "minutes:seconds" (string) to seconds (int)
    """
    minutes_col = 0
    seconds_col = 1
    minutes_seconds = album_length.split(":")
    total_seconds = (int(minutes_seconds[minutes_col])*60) + (int(minutes_seconds[seconds_col]))
    return total_seconds

def get_total_albums_length(albums):
    """
    Get sum of lengths of all albums in minutes, rounded to 2 decimal places
    Example: 3:51 + 5:20 = 9.18             
             231 + 320 seconds = 551 seconds

    :param list albums: albums' data
    :returns: total albums' length in minutes
    :rtype: float
    """
    sum_of_seconds = 0
    for album in albums:
        sum_of_seconds += to_time(album[length_col])

    minutes = round((sum_of_seconds / 60),2)
    return minutes