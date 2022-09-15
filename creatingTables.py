import sqlite3 as lit

def main():
    try:
        db = lit.connect('employee.db')
        cur = db.cursor()

        tablequery = 