import sqlite3
import sys 
from app import *

filename='results.csv'

data = getfile(filename)
data = data[1:]
data = caps(data)
data = removeduplicates(data)
data = question3validation(data)


def main():
    db = sqlite3.connect('answers.db')
    create_answers_table(db)
    show_tables(db)
    describe_table(db, 'answers')
    insert_data(db,'answers',data)
    db.close()

if __name__ == '__main__':
    sys.exit(main())



