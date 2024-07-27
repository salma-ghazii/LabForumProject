from flask import Flask, render_template, request, jsonify, session
from database import connect_db, create_tables, insert_lab, delete_lab, get_labs, insert_post, get_posts, delete_post, insert_user, authenticate_user, get_user_id, delete_table

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key for session management

@app.route('/')
def index():
    delete_table("users")
    delete_table("posts")
    delete_table("labs")
    create_tables()
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return 'Username and password are required', 400
    insert_user(username, password)
    return '', 204

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if authenticate_user(username, password):
        session['username'] = username
        return '', 204
    return 'Invalid credentials', 401

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return '', 204

@app.route('/labs', methods=['GET', 'POST'])
def labs():
    if request.method == 'POST':
        if 'username' not in session:
            print("test")
            return 'Unauthorized', 401
        data = request.get_json()
        location = data.get('location')
        insert_lab(location)
        return '', 204
    else:
        labs = get_labs()
        # print("labs" + str(labs))
        return jsonify([{'LabID': row[0], 'Location': row[1]} for row in labs])

@app.route('/labs/<int:id>', methods=['DELETE'])
def delete_lab_route(id):
    if 'username' not in session:
        return 'Unauthorized', 401
    delete_lab(id)
    return '', 204

@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        if 'username' not in session:
            return 'Unauthorized', 401
        data = request.get_json()
        lab_id = data.get('labid')
        user_id = get_user_id(session['username'])
        post_content = data.get('postContent')
        insert_post(lab_id, user_id, post_content)
        return '', 204
    else:
        posts = get_posts()
        print("posts" + str(posts))
        return jsonify([{'PostID': row[0], 'LabID': row[1], 'UserID': row[2], 'PostContent': row[3]} for row in posts])

@app.route('/posts/<int:id>', methods=['DELETE'])
def delete_post_route(id):
    if 'username' not in session:
        return 'Unauthorized', 401
    delete_post(id)
    return '', 204

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
