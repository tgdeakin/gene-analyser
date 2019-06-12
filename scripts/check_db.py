def is_sqlite3(filename):

    from os.path import isfile, getsize

    if not isfile(filename):
        return False
    if getsize(filename) < 100:  # SQLite database file header is 100 bytes
        return False

    with open(filename, 'rb') as fd:
        header = fd.read(100)
        fd.close()
    return header[:16] == b'SQLite format 3\000'
