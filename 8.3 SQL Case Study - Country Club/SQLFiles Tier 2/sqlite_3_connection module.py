# IMPORT SQLITE3 AND SQLITE3 ERROR FOR THE CONNECTION MODULE
import sqlite3
from sqlite3 import Error

# CREATE FUNCTIONS TO ESTABLISH AND CLOSE CONNECTION TO DATABASE AND TEST FUNCTION

# CREATE A CONNECTION TO A DATABASE
def create_connection(db_file):
    """ Establish a connection to the database specified by 
        the db_file

    Args:
        db_file (string): contains information to establish
                          a connection to a database and returns
                          the Connection Object or None.
    """
    conn = None
    try:
       conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

# CREATE A TEST FUNCTION THAT SELECTS ALL TASKS
def select_all_tasks(conn):
    """Query all rows in the tasks table

    Args:
        conn (Connection Object): The Connection Object to
                                  execute tasks returns None.
    """
    cur = conn.cursor()
    
    query = """
        SELECT *
        FROM FACILITIES
        """
        
    cur.execute(query)
    
    rows = cur.fetchall()
    
    for row in rows:
        print(row)
        
# MAIN FUNCTION
def main():
    database = "sqlite_db_pythonsqlite.db"
    
    # establish a connection
    conn = create_connection(database)
    with conn:
        print("2. Query all tasks")
        select_all_tasks(conn)
        
if __name__ == "__main__":
    main()