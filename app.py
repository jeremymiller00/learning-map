import sys
import typer
import sqlite3
from uuid import uuid4
from src.learningmap.crud import *
from configs.learningmap.config import set_config

app = typer.Typer()

@app.command()
def main(cmd: str,):

    interactive = False
    config = set_config()
    cur, con = connect(config.get("db_path"))

    if cmd == "interactive":
        interactive = True
        while interactive:
            cmd = input("Enter a command (add, getall, query, quit): ")
            if cmd == "quit":
                break
            else:
                execute(cmd, cur, con)        
    else:
        execute(cmd, cur, con)


def execute(cmd, cur, con):
    if cmd == "add":
        try:
            add_item(cur, con)
        except sqlite3.OperationalError:
            print("Exception caught")
    elif cmd == "getall":
        for i in get_all(cur, con):
            print(i)
    elif cmd == "query":
        try:
            for i in query(cur, con):
                print(i)
        except sqlite3.OperationalError as e:
            print(f"Exception raised: {e}")
    else:
        typer.echo(f"Entered {cmd}")


if __name__ == "__main__":
    app()