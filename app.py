from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from database import connect_db, create_tables, insert_lab, insert_post, get_labs, get_posts, delete_lab, delete_post, get_user_id, insert_user, authenticate_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

@app.route('/')
def index():
    """Render the home page."""
    username = session.get('username')
    return render_template('index.html', username=username)

@app.route('/labs_page')
def add_lab_page():
    """Render the page to add labs."""
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session.get('username')
    return render_template('labs.html', username=username)

@app.route('/posts_page')
def add_post_page():
    """Render the page to add posts."""
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session.get('username')
    return render_template('posts.html', username=username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login."""
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        if authenticate_user(username, password):
            session['username'] = username
            return '', 204
        else:
            return jsonify({'error': 'Invalid credentials'}), 401
    
    username = session.get('username')
    return render_template('login.html', username=username)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handle user registration."""
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({'error': 'Username and password required'}), 400
        
        insert_user(username, password)
        return '', 204
    
    username = session.get('username')
    return render_template('register.html', username=username)

@app.route('/logout', methods=['POST'])
def logout():
    """Handle user logout."""
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/labs', methods=['GET', 'POST'])
def labs():
    """Handle requests related to labs."""
    if request.method == 'POST':
        if 'username' not in session:
            return 'Unauthorized', 401
        data = request.get_json()
        location = data.get('location')
        insert_lab(location)
        return '', 204
    else:
        labs = get_labs()
        return jsonify([{'LabID': row[0], 'Location': row[1]} for row in labs])

@app.route('/posts', methods=['GET', 'POST'])
def posts():
    """Handle requests related to posts."""
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
        return jsonify([{'PostID': row[0], 'LabID': row[1], 'UserID': row[2], 'PostContent': row[3]} for row in posts])

@app.route('/labs/<int:id>', methods=['DELETE'])
def delete_lab_route(id):
    """Handle deletion of a lab."""
    delete_lab(id)
    return '', 204

@app.route('/posts/<int:id>', methods=['DELETE'])
def delete_post_route(id):
    """Handle deletion of a post."""
    delete_post(id)
    return '', 204

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
    
