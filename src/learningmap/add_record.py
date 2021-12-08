"""
Add a record to the learning map db

(id TEXT, item TEXT, competency INTEGER, type TEXT, is_repeating INTEGER,
is_ds_gold INTEGER, date_started TEXT, date_finished TEXT,
status TEXT, notes TEXT, links TEXT);

"Hugingface Course"
https://huggingface.co/course/chapter1/1

"""

from sys import exit, argv
from uuid import uuid4
import sqlite3
# import configs.config as config

def connect(db_path):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    return con, cur

def main(db_path):
    con, cur = connect(db_path)
    item = input("Item name: ")
    competency = int(input("Competency (1:ML, 2:SWE, 3:PM, 4:Company): "))
    type = input("Type (Course, Book, Tutorial, Article): ")
    is_repeating = int(input("Repeating (1:Y, 0:N)?: "))
    is_ds_gold = int(input("DS Gold (1:Y, 0:N)?: "))
    date_started = input("Date Started (2021-01-01)?: ")
    date_finished = input("Date Finished (2021-01-01)?: ")
    status = input("Status (To_Do, In_Progress, On_Hold, Done)? ")
    notes = input("Notes: ")
    links = input("Links: ")
    
    cur_str = '''INSERT INTO items VALUES 
                (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

    cur.execute(cur_str, (str(uuid4()), item.strip(), competency, 
                    type.strip(), is_repeating, is_ds_gold, date_started.strip(), 
                    date_finished.strip(), status.strip(), notes.strip(), 
                    links.strip()))
    con.commit()
    print("Record successfully added:")
    print(f"{item.strip()}, {competency}, {type.strip()}, {is_repeating}, {is_ds_gold}, {date_started.strip()}, {date_finished.strip()}, {status.strip()}, {notes.strip()}, {links.strip()}")

if __name__ == "__main__":
    # temp hack
    db_path = "data/learningmap.db"
    main(db_path)

    