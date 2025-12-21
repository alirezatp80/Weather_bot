import sqlite3

def create_table():
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS users(
                           id INTEGER PRIMARY_KEY ,
                           name TEXT,
                           location TEXT
                       )
                       ''')
        conn.commit()
        
def insert_user(id , name , location):
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
                       INSERT INTO users(id, name, location)
                       VALUES (?, ?, ?)
                       ''', (id, name, location))
        conn.commit()


def select_user(id):
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT * FROM users WHERE id = ?
                       """, (id,))
        return cursor.fetchone()

def select_alluser():
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        return cursor.fetchall()
    
def update_location(id,newlocation):
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
                       UPDATE users SET location = ? WHERE id = ?
                       """, (newlocation, id))
        conn.commit()


