from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from tabulate import tabulate

# Initialize the Flask app
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a simple model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Create the database tables
with app.app_context():
    db.create_all()

# POST route to add a user
@app.route("/add_user", methods=["POST"])
def add_user():
    # Get JSON data from the request
    data = request.get_json()

    # Extract data from the JSON
    username = data.get('username')

    if not username:
        return jsonify({"error": "Username is required"}), 400  # 400 Bad Request

    # Create a new User instance and add to the database
    new_user = User(username=username)
    db.session.add(new_user)
    db.session.commit()

    # Return a success message in JSON format
    return jsonify({"message": f"User {username} added successfully!"}), 201  # 201 Created

# GET route to retrieve all users
@app.route("/users", methods=["GET"])
def get_users():
    all_users = User.query.all()
    users_list = [{"id": user.id, "username": user.username} for user in all_users]
    
    # Extract column names for the table
    headers = ["ID", "Username"]
    
    # Format the data for tabulate
    table_data = [(user.id, user.username) for user in all_users]
    
    # Use tabulate to format the table
    formatted_table = tabulate(table_data, headers=headers, tablefmt="pretty")
    
    # Print the table to console
    print(formatted_table)
    
    # Return the table data as a JSON response
    return jsonify(users_list)


# DELETE route to remove a user by username
@app.route("/delete_user/<username>", methods=["DELETE"])
def delete_user(username):
    # Find the user by username
    user = User.query.filter_by(username=username).first()

    # If the user doesn't exist, return an error message
    if not user:
        return jsonify({"error": f"User with username {username} not found"}), 404  # 404 Not Found

    # Delete the user
    db.session.delete(user)
    db.session.commit()

    # Return a success message
    return jsonify({"message": f"User {username} deleted successfully!"}), 200  # 200 OK


# Define a route
@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
