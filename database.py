import sqlite3

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
    """Insert a new lab into the database."""
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
