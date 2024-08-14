# Creat a class Database that connects to a database and provides methods to execute queries. Handle exceptions if connection fail.
import sqlite3
class Database: 
    def __init__(self, db_file = "mydatabase.db"):
        try:
            self.conn = sqlite3.connect(db_file)
            print("successfull connect to database")
        except:
            print("error : can not connect to database")
            self.conn = None
    
    def execute(self, query):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(query) .self.conn.commit()
                return cursor.fetchall()
            except:
                print("mistake in execute command")
        else:
            print("error: first connect to database")

db = Database()
results = db.execute("SELECT * FROM my_table")
if results:
    for row in results:
        print(row)