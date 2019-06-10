import sqlite3
from populate_db import populate_db


def refresh_db():

    # Creates or opens a file called mydb with a SQLite3 DB
    db = sqlite3.connect('data/mydb')

    cursor = db.cursor()
    cursor.execute('''
        DELETE FROM genes
    ''')

    cursor.execute('''
        DELETE FROM human_gene_coords
    ''')

    cursor.execute('''
        DELETE FROM human_mirna_coords
    ''')

    db.commit()
    populate_db()
    db.close()
