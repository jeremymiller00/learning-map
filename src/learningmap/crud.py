"""
Add a record to the learning map db

(id TEXT, item TEXT, competency INTEGER, type TEXT, is_repeating INTEGER,
is_ds_gold INTEGER, date_started TEXT, date_finished TEXT,
status TEXT, notes TEXT, links TEXT);
"""

from uuid import uuid4
import sqlite3

def connect(db_path):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    return con, cur

def add_item(cur, con):
    item = input("Item name: ")
    
    competency = 0
    while competency not in [1,2,3,4]:
        competency = int(input("Competency (1:ML, 2:SWE, 3:PM, 4:Company): "))
    
    type = ""
    while type not in ["Course," "Book", "Tutorial", "Article"]:
        type = input("Type (Course, Book, Tutorial, Article): ")
    
    is_repeating = 99
    while is_repeating not in [0,1]:
        is_repeating = int(input("Repeating (1:Y, 0:N)?: "))
    
    is_ds_gold = 99
    while is_ds_gold not in [0.1]:
        is_ds_gold = int(input("DS Gold (1:Y, 0:N)?: "))
    
    date_started = input("Date Started (2021-01-01)?: ")
    date_finished = input("Date Finished (2021-01-01)?: ")
    
    status= ""
    while status not in ["To_Do", "In_Progress", "On_Hold", "Done"]:
        status = input("Status (To_Do, In_Progress, On_Hold, Done)? ")
    notes = input("Notes (optional): ")
    links = input("Links (optional): ")
    
    cur_str = '''INSERT INTO items VALUES 
                (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

    # cur.execute(cur_str, (str(uuid4()), item.strip(), competency, 
    #                 type.strip(), is_repeating, is_ds_gold, date_started.strip(), 
    #                 date_finished.strip(), status.strip(), notes.strip(), 
    #                 links.strip()))
    # con.commit()
    print("Record successfully added:")
    print(f"{item.strip()}, {competency}, {type.strip()}, {is_repeating}, {is_ds_gold}, {date_started.strip()}, {date_finished.strip()}, {status.strip()}, {notes.strip()}, {links.strip()}")
    return

def get_all(cur, con, table="ITEMS"):
    cur_str = f'''SELECT * FROM {table}'''
    return cur.execute(cur_str)

def query(cur, con):
    query = input("Query: ")
    return cur.execute(query)

def add(a,b):
    return a+b