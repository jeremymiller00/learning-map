"""
python src/initialsetup/build_database.py data/items.csv data/competencies.csv data/learningmap.db
"""
from sys import exit, argv
from uuid import uuid4
import sqlite3

def connect(db_path):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    return con, cur

def create_tables(con, cur):
    cur.execute('''CREATE TABLE IF NOT EXISTS items
               (id TEXT, item TEXT, competency INTEGER, type TEXT, is_repeating INTEGER, 
               is_ds_gold INTEGER, date_started TEXT, date_finished TEXT,
               status TEXT, notes TEXT, links TEXT)''')

    cur.execute('''CREATE TABLE IF NOT EXISTS competencies
               (id INTEGER PRIMARY KEY, name TEXT, notes TEXT)''')
    con.commit()
    return

# load data
def load_data(raw_data_path):
    with open(raw_data_path, "r") as file:
        data = file.readlines()
    return data[1:] # skip header

# insert data
def insert_data(data_path, con, cur, table):
    if table not in ["items", "competencies"]:
        raise ValueError("Table must be in [items, competencies]")
    data = load_data(data_path)
    if table == "items":
        for row in data:
            values = row.split(",")
            cur_str = '''INSERT INTO items VALUES 
                (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            cur.execute(cur_str, (str(uuid4()), values[0], values[1], 
                    values[2],  values[3], values[4], values[5], values[6],
                    values[7], values[8], values[9].strip()))

    elif table == "competencies":
        for row in data:
            values = row.split(",")
            cur_str = '''INSERT INTO competencies VALUES (?, ?, ?)'''
            cur.execute(cur_str, (values[0], values[1], values[2].strip()))
    con.commit()

def main(item_data_path, competency_data_path, db_path):
    con, cur = connect(db_path)
    create_tables(con, cur)
    insert_data(item_data_path, con, cur, table="items")
    insert_data(competency_data_path, con, cur, table="competencies")
    con.close()



#######################################

if __name__ == '__main__':
    # item_data_path = sys.argv[1]
    # competency_data_path = sys.argv[2]
    # db_path = sys.argv[3]
    if len(argv) != 4:
        print("Usage: python [script_path] [item_data_path] [competency_data_path] [db_path]")
        exit(1)
    main(argv[1], argv[2], argv[3])
    exit(0)
