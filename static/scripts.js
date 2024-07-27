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
                        Lab ID: ${lab[0]}, Location: ${lab[1]}
                        <span class="delete-btn" onclick="deleteLab(${lab[0]})">X</span>
                    </div>
                `;
            });
        });
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
                        Post ID: ${post[0]}, Lab ID: ${post[1]}, User ID: ${post[2]}, Content: ${post[3]}
                        <span class="delete-btn" onclick="deletePost(${post[0]})">X</span>
                    </div>
                `;
            });
        });
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
    const userid = document.getElementById('postUserID').value;
    const postContent = document.getElementById('postContent').value;
    fetch('/posts', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ labid, userid, postContent })
    }).then(() => {
        document.getElementById('postLabID').value = '';
        document.getElementById('postUserID').value = '';
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
