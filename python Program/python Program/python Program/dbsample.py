import sqlite3
from flask import *
from werkzeug.exceptions import abort


def get_db_connection():
    conn = sqlite3.connect('pythonsqlite.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id):
    conn = get_db_connection()
    print("inside")
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    for r in post:
        print(r)
    conn.close()
    if post is None:
        abort(404)
    return post

def main():
    id=input("enter the id of post")
    get_post(id);

if __name__ == '__main__':
    main()

