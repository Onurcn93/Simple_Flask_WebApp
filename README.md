# Flask-JS User Management App

This project is a simple web application that demonstrates how to manage users using a Flask backend and a JavaScript-powered frontend. Users can be added dynamically via JavaScript event listeners, and the user list is updated without reloading the page.

## Features

- Add a new user dynamically via a JavaScript-powered interface.
- Display all users stored in the database.
- Use Flask as the backend to handle user data and database operations.
- Use JavaScript `fetch()` to interact with Flask API endpoints asynchronously.
- Display success or error messages dynamically on the frontend.

## Technologies Used

- **Flask** (Python)
- **SQLite** (Database)
- **HTML/CSS** (Frontend)
- **JavaScript** (Frontend logic, `fetch` API for backend interaction)

## Project Structure

```
.
├── app.py                 # Flask application
├── templates
│   └── index.html         # Frontend HTML
├── static
│   ├── css
│   │   └── style.css      # Styling for the app
│   └── js
│       └── script.js      # Frontend JavaScript logic
└── README.md              # Project README file
```

## API Endpoints

### 1. Add User
**Endpoint**: `/add_user`
- **Method**: POST
- **Request Body**: JSON object with the following structure:
  ```json
  {
      "username": "<username>"
  }
  ```
- **Response**:
  - Success: `{"message": "User <username> added successfully!"}`
  - Error: `{"error": "Username is required"}`

### 2. Get All Users
**Endpoint**: `/users`
- **Method**: GET
- **Response**:
  - Array of users:
    ```json
    [
        {"id": 1, "username": "Alice"},
        {"id": 2, "username": "Bob"}
    ]
    ```

## Frontend Interaction

### Adding Users
- Enter a username in the input field and click the **Save User** button.
- JavaScript captures the button click event, sends a `POST` request to the `/add_user` endpoint, and updates the user list dynamically without refreshing the page.

### Viewing Users
- The users are displayed in a list on the homepage, which updates dynamically when a new user is added.

---

### Author
Developed by Onurcn93 (https://github.com/Onurcn93).
