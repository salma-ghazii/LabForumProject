// Displays labs and posts upon website arrival
document.addEventListener('DOMContentLoaded', () => {
    fetchLabs();
    fetchPosts();
});

// Get all labs then display on html
function fetchLabs() {
    fetch('/labs')
        .then(response => response.json())
        .then(data => {
            const labsDiv = document.getElementById('labs');
            labsDiv.innerHTML = '';
            data.forEach(lab => {
                labsDiv.innerHTML += `
                    <div class="lab">
                        Lab ID: ${lab.LabID}, Location: ${lab.Location}
                        <span class="delete-btn" onclick="deleteLab(${lab.LabID})">X</span>
                    </div>
                `;
            });
        })
        .catch(error => console.error('Error fetching labs:', error));
}

// Get all posts then display on html
function fetchPosts() {
    fetch('/posts')
        .then(response => response.json())
        .then(data => {
            const postsDiv = document.getElementById('posts');
            postsDiv.innerHTML = '';
            data.forEach(post => {
                postsDiv.innerHTML += `
                    <div class="post">
                        Post ID: ${post.PostID}, Lab ID: ${post.LabID}, User ID: ${post.UserID}, Content: ${post.PostContent}
                        <span class="delete-btn" onclick="deletePost(${post.PostID})">X</span>
                    </div>
                `;
            });
        })
        .catch(error => console.error('Error fetching posts:', error));
}


// Adds lab to the database and rerenders display with added content
function addLab() {
    const location = document.getElementById('labLocation').value;
    fetch('/labs', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ location })
    }).then(() => {
        document.getElementById('labLocation').value = '';
        fetchLabs();
    });
}

// Adds post to the database and rerenders display with added content
function addPost() {
    const labid = document.getElementById('postLabID').value;
    // const userid = document.getElementById('postUserID').value;
    const postContent = document.getElementById('postContent').value;
    fetch('/posts', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ labid, postContent })
    }).then(() => {
        document.getElementById('postLabID').value = '';
        // document.getElementById('postUserID').value = '';
        document.getElementById('postContent').value = '';
        fetchPosts();
    });
}

// Deletes a lab from the database
function deleteLab(id) {
    fetch(`/labs/${id}`, {
        method: 'DELETE'
    }).then(() => {
        fetchLabs();
    });
}

// Deletes a post from the database
function deletePost(id) {
    fetch(`/posts/${id}`, {
        method: 'DELETE'
    }).then(() => {
        fetchPosts();
    });
}

// User registration
function register() {
    const username = document.getElementById('regUsername').value;
    const password = document.getElementById('regPassword').value;
    fetch('/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    }).then(() => {
        document.getElementById('regUsername').value = '';
        document.getElementById('regPassword').value = '';
        alert('Registration successful');
    }).catch(error => {
        console.error('Error:', error);
    });
}

// User login
function login() {
    const username = document.getElementById('loginUsername').value;
    const password = document.getElementById('loginPassword').value;
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    }).then(response => {
        if (response.ok) {
            document.getElementById('loginUsername').value = '';
            document.getElementById('loginPassword').value = '';
            alert('Login successful');
            fetchLabs();  // Optionally fetch data after login
            fetchPosts();
        } else {
            alert('Invalid credentials');
        }
    }).catch(error => {
        console.error('Error:', error);
    });
}

// User logout
function logout() {
    fetch('/logout', {
        method: 'POST'
    }).then(() => {
        alert('Logged out');
        fetchLabs();  // Optionally fetch data after logout
        fetchPosts();
    }).catch(error => {
        console.error('Error:', error);
    });
}

// Existing functions (fetchLabs, fetchPosts, addLab, addPost, deleteLab, deletePost) remain the same
