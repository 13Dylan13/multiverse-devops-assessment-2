import sqlite3
import sys 
from app import *

def main():
    db = sqlite3.connect('answers.db')
    create_answers_table(db)
    show_tables(db)
    describe_table(db,'answers')
    data = select_all(db, 'answers')
    output_results(data)
    data = formatForPrinting(data)
    db.close()

if __name__ == '__main__':
    sys.exit(main())

