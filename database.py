import sqlite3

"""
Defines Database Methods for insertion/deletion and creation of schema
"""

def connect_db():
    """Connect to the SQLite database."""
    conn = sqlite3.connect('lab_forum.db')
    return conn

def create_tables():
    """Create tables in the database."""
    conn = connect_db()
    cursor = conn.cursor()
    with open('LabForumProject\\db\\schema.sql', 'r') as f:
        schema = f.read()
    cursor.executescript(schema)
    conn.commit()
    conn.close()

def insert_lab(location):
    """Insert a new lab into the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO labs (Location) VALUES (?)', (location,))
    conn.commit()
    conn.close()

def delete_lab(labid):
    """Delete a lab into the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM labs WHERE LabID == ?', (labid,))
    conn.commit()
    conn.close()

def get_labs():
    """Retrieve all labs from the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM labs')
    rows = cursor.fetchall()
    conn.close()
    return rows


def insert_post(labid, userid, postContent):
    """Insert a new post into the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO posts (LabID, UserID, PostContent) VALUES (?, ?, ?)', (labid, userid, postContent,))
    conn.commit()
    conn.close()


def get_posts():
    """Retrieve all labs from the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM posts')
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_post(postid):
    """Retrieve a post from the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM posts WHERE PostID == ?', (postid,))
    conn.commit()
    conn.close()


def delete_table(table):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f'DROP TABLE IF EXISTS {table};')
    conn.commit()
    conn.close()
