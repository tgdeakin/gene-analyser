from collections import defaultdict
import sqlite3


def run_analysis(genes_of_interest):

    genes = []
    genes_to_count = []
    gene_dict = defaultdict(list)

    # Creates or opens a file called mydb with a SQLite3 DB
    db = sqlite3.connect('data/mydb')

    cursor = db.cursor()

    for gene in genes_of_interest.split(" "):
        gene_to_append = cursor.execute('''SELECT mirna_target_gene, mirna FROM genes WHERE mirna_target_gene=(?)''',
                                        (gene,)).fetchall()

        genes.append(gene_to_append)

    for gene in genes:
        for entry in gene:
            genes_to_count.append((entry[0], entry[1]))

    for k, v in genes_to_count:
        gene_dict[k].append(v)

    for k, v in gene_dict.items():
        gene_coords = cursor.execute(
            '''SELECT chromosome_name, gene_start, gene_end FROM human_gene_coords WHERE gene_name=(?)''',
            (k,)).fetchall()

        unique_interactions = list(set(v))
        mirna_coords_to_display = ''
        coords_to_display = ''

        for mirna in unique_interactions:
            split_mirna = mirna.split("-")
            if len(split_mirna) == 4:
                del split_mirna[-1]

            join_chromosome = str.join('-', split_mirna)

            mirna_coords = cursor.execute(
                        '''SELECT chromosome_name, gene_start, gene_end FROM human_mirna_coords WHERE mirbase_id=(?)''',
                        (join_chromosome.lower(),)).fetchall()

            mirna_coord = ''

            for coord in mirna_coords:
                mirna_coord += mirna + "[" + coord[0] + ":" + str(coord[1]) + "-" + str(coord[2]) + "] "
                mirna_coords_to_display += mirna_coord

        for coord in gene_coords:
            coords_to_display += (coord[0] + ": " + str(coord[1]) + '-' + str(coord[2]))

        print("There should be " + str(len(unique_interactions)) + " interaction(s) , but you have " + str(len(unique_interactions) - len(set(mirna_coords_to_display.strip().split(" ")))) + " missing interaction(s)")

        print(k, '[', coords_to_display, ']', ':', str(len(set(mirna_coords_to_display.strip().split(" ")))) + " interactions", "-", set(mirna_coords_to_display.strip().split(" ")))
