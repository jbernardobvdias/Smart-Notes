async function signup() {
    let username = document.getElementById("email").value;
    let password = document.getElementById("password").value;

    if (!username || !password) {
        alert("Please enter both username and password.");
        return;
    }

    const response = await fetch('/api/signup/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
    });
    const data = await response.json();
    console.log(data);
}

async function login(username, password) {
    const response = await fetch('/api/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
    });
    const data = await response.json();
    console.log(data);
}

async function saveNote(title, content) {
    const response = await fetch('/api/save-note/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ title, content }),
    });
    const data = await response.json();
    console.log(data);
}

async function getNotes() {
    const response = await fetch('/api/get-notes/');
    const data = await response.json();
    console.log(data);
}

async function deleteNote(noteId) {
    const response = await fetch('/api/delete-note/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ id: noteId }),
    });
    const data = await response.json();
    console.log(data);
}

async function askQuestion(question) {
    const response = await fetch('/api/ask/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question }),
    });
    const data = await response.json();
    console.log(data);
}