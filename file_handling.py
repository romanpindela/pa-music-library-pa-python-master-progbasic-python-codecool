def import_data(filename='albums_data.txt') -> list:
    """
    Import data from a file to a list. Expected returned data format:
        ["David Bowie", "Low", "1977", "rock", "38:26"],
        ["Britney Spears", "Baby One More Time", "1999", "pop", "42:20"],
        ...]

    :param str filename: optional, name of the file to be imported

    :returns: list of lists representing albums' data
    :rtype: list
    """
    try:
        table_data = []
        with open(filename) as file:
            for line in file:
                line = line.strip('\n')
                columns = line.split(",")
                table_data.append(columns)
        return table_data
    except FileNotFoundError:
        print("File not found!")



def export_data(albums, filename='albums_data.txt', mode='a'):
    """
    Export data from a list to file. If called with mode 'w' it should overwrite
    data in file. If called with mode 'a' it should append data at the end.

    :param list albums: albums' data
    :param str filename: optional, name of file to export data to
    :param str mode: optional, file open mode with the same meaning as\
    file open modes used in Python. Possible values: only 'w' or 'a'

    :raises ValueError: if mode other than 'w' or 'a' was given. Error message:
        'Wrong write mode'
    """
    if mode == 'a' or mode == 'w':
        artist_col = 0
        album_col = 1
        year_col = 2
        genre_col = 3
        length_col = 4

        with open(filename, mode) as file:
            for album in albums:
                file.write(f"{album[artist_col]},{album[album_col]},{album[year_col]},{album[genre_col]},{album[length_col]}\n")
    else:
        raise ValueError("Wrong write mode")

