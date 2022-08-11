import keywords as K
import sqlite3
import random
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_tasks(conn,id):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM GPA_DETAILS WHERE id=?",[id])
    rows = cur.fetchall()
    for row in rows:
        print(row)
def select_student(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM STUD_INFO WHERE id=?", (priority,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

def select_all_tasks1(conn,id):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute(" select sum(salary),avg(salary),max (salary),min(salary),count(*) from COMPANY where address=?",[id])
    rows = cur.fetchall()
    for row in rows:
        print(row)


def main():
    database = r"C:\Users\Besant\Downloads\flask-templates-exampl\seminar2_progress\shrya\sqlite\db\training.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1.print student info detail:")
        idinput=int(input("enter the id of student"))
        select_student(conn,idinput)

        print("2. print all CPGA")
        select_all_tasks(conn,idinput)
        print("3. compnay information for state")
        state=input('enter the state')
        select_all_tasks1(conn,state)
  

if __name__ == '__main__':
    main()

