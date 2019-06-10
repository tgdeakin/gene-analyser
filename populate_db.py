import sqlite3


def populate_db():

    with open('/Users/tdeakin/Downloads/genes.txt', encoding="utf8", errors='ignore') as human_genes:
        genes = [human_gene.strip().split("\t") for human_gene in human_genes]

    human_genes.close()

    with open('/Users/tdeakin/Downloads/Ch38.p12 Human Gene coordinates.txt', encoding="utf8",
              errors='ignore') as human_gene_coordinates:
        hgcs = [human_gene_coordinate.strip().split("\t") for human_gene_coordinate in human_gene_coordinates]

    human_gene_coordinates.close()

    with open('/Users/tdeakin/Downloads/Ch38.p12 Human miRNA coordinates.txt', encoding="utf8",
              errors='ignore') as human_mirna_coordinates:
        hmirna = [human_mirna_coordinate.strip().split("\t") for human_mirna_coordinate in human_mirna_coordinates]

    human_mirna_coordinates.close()

    # Creates or opens a file called mydb with a SQLite3 DB
    db = sqlite3.connect('data/mydb')

    cursor = db.cursor()

    cursor.executemany('''
        INSERT INTO genes(mirtarbase_id,
                          mirna,
                          species,
                          mirna_target_gene,
                          target_gene,
                          species_target_gene,
                          experiments,
                          support_type,
                          refs)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', genes)

    cursor.executemany('''
        INSERT INTO human_gene_coords(gene_name,
                          chromosome_name,
                          gene_start,
                          gene_end)
        VALUES(?, ?, ?, ?)
    ''', hgcs)

    cursor.executemany('''
        INSERT INTO human_mirna_coords(gene_name,
                          mirbase_id,
                          chromosome_name,
                          gene_start,
                          gene_end)
        VALUES(?, ?, ?, ?, ?)
    ''', hmirna)

    db.commit()
    db.close()
