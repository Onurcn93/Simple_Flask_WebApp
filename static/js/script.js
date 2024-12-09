document.addEventListener("DOMContentLoaded", function() {
    const saveButton = document.getElementById('save-user-btn');
    const usernameInput = document.getElementById('username');
    const userList = document.getElementById('user-list');
    const messageDiv = document.getElementById('message');

    saveButton.addEventListener('click', function() {
        const username = usernameInput.value.trim();

        if (!username) {
            messageDiv.textContent = "Username cannot be empty.";
            messageDiv.style.color = "red";
            return;
        }

        // Clear any previous messages
        messageDiv.textContent = '';

        // Send POST request to add the user
        fetch("/add_user", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ username: username })
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                // Display success message
                messageDiv.textContent = data.message;
                messageDiv.style.color = "green";

                // Update the user list without reloading the page
                fetch("/users")
                .then(response => response.json())
                .then(users => {
                    userList.innerHTML = '';  // Clear the current user list
                    users.forEach(user => {
                        const listItem = document.createElement('li');
                        listItem.textContent = `ID: ${user.id}, Username: ${user.username}`;
                        userList.appendChild(listItem);
                    });
                });
            } else if (data.error) {
                // Display error message
                messageDiv.textContent = data.error;
                messageDiv.style.color = "red";
            }
        })
        .catch(error => {
            console.error('Error:', error);
            messageDiv.textContent = "An error occurred while adding the user.";
            messageDiv.style.color = "red";
        });

        // Clear the input field
        usernameInput.value = '';
    });
});
