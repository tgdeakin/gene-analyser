from analysis import run_analysis
from update_db import refresh_db
from check_db import is_sqlite3
from create_db import create_db


def main():

    genes_of_interest = input("Enter the genes you want to look up, separated by a space: ")
    confirmation = input("You entered these genes: " + genes_of_interest.strip() + ". Is that right? Enter y/n: ")

    if confirmation == 'y':
        # Check if the database already exists
        print("Checking if databases exist...")
        if is_sqlite3('./data/mydb'):
            # If it does, ask if user wants to update it
            update_database = input("Do you want to update your database before running analysis? Enter y/n: ")
            if update_database == 'y':
                # Do the updating
                print("Updating databases...")
                refresh_db()
        else:
            # Otherwise create the database
            print("Creating databases...")
            create_db()
        # Then run the analysis
        run_analysis(genes_of_interest)

    elif confirmation == "n":
        print('Exiting! Bye bye.')


main()
