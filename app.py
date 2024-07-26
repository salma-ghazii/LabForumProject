# import database

# # Just messing around to make sure the database works
# database.connect_db()
# # # database.insert_lab("Newark, NJ")
# # print(database.get_labs())
# # database.delete_lab(1)
# # print(database.get_labs())
# # database.delete_table("posts")
# # database.create_tables()
# # database.insert_post(1, 2, "testing")
# # print(database.get_posts())


from flask import Flask, request, jsonify, render_template
import sqlite3
import database

app = Flask(__name__)


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/labs', methods=['GET', 'POST'])
def manage_labs():
    """Retrieve all labs or add a new lab."""
    if request.method == 'POST':
        location = request.json.get('location')
        conn = database.connect_db()
        database.create_tables()
        print("Tables Created")
        cursor = conn.cursor()
        cursor.execute('INSERT INTO labs (Location) VALUES (?)', (location,))
        conn.commit()
        conn.close()
        return jsonify({'status': 'Lab added'}), 201

    elif request.method == 'GET':
        conn = database.connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM labs')
        rows = cursor.fetchall()
        conn.close()
        return jsonify(rows)

@app.route('/labs/<int:labid>', methods=['DELETE'])
def delete_lab(labid):
    """Delete a lab."""
    conn = database.connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM labs WHERE LabID = ?', (labid,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'Lab deleted'})

@app.route('/posts', methods=['GET', 'POST'])
def manage_posts():
    """Retrieve all posts or add a new post."""
    if request.method == 'POST':
        labid = request.json.get('labid')
        userid = request.json.get('userid')
        postContent = request.json.get('postContent')
        conn = database.connect_db()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO posts (LabID, UserID, PostContent) VALUES (?, ?, ?)', (labid, userid, postContent))
        conn.commit()
        conn.close()
        return jsonify({'status': 'Post added'}), 201

    elif request.method == 'GET':
        conn = database.connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM posts')
        rows = cursor.fetchall()
        conn.close()
        return jsonify(rows)

if __name__ == '__main__':
    app.run(debug=True)