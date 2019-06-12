import sqlite3
from scripts.populate_db import populate_db


def create_db():

    # Creates or opens a file called mydb with a SQLite3 DB
    db = sqlite3.connect('data/mydb')

    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS genes(id INTEGER PRIMARY KEY, mirtarbase_id TEXT, mirna TEXT,
                                         species TEXT, mirna_target_gene TEXT, target_gene INTEGER,
                                         species_target_gene TEXT, experiments TEXT, support_type TEXT, refs TEXT)
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS human_gene_coords(id INTEGER PRIMARY KEY, gene_name TEXT,
                                                     chromosome_name TEXT, gene_start INTEGER, gene_end INTEGER)
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS human_mirna_coords(id INTEGER PRIMARY KEY, gene_name TEXT,
                                                     mirbase_id TEXT, chromosome_name TEXT, 
                                                     gene_start INTEGER, gene_end INTEGER)
    ''')

    populate_db()
    db.commit()
    db.close()
