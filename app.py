from sqlalchemy.orm import Session
from db import SessionLocal, engine, Base
from flask import Flask, jsonify, request 
from models import User  # Import User from models.py

# Initialize Flask app
app = Flask(__name__)


# Route to get all users from the 'users' table
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    session = SessionLocal()
    user = session.get(User, user_id) 
    if user:
        return jsonify({"id": user.id, "name": user.name, "email": user.email}), 200
    else:
        return jsonify({"error": "User not found"}), 404
    
@app.route('/users', methods=['GET'])
def get_all_users():
    with SessionLocal() as session:
        # Query all users
        users = session.query(User).all()
        
        # Convert users to a list of dictionaries
        users_list = [{"id": user.id, "name": user.name, "email": user.email} for user in users]
        
        return jsonify(users_list), 200    

@app.route('/users', methods=['POST'])
def create_user():
    session = SessionLocal()
    data = request.get_json()  # Get JSON data from request body

    # Check if required fields are present
    if "name" not in data or "email" not in data:
        return jsonify({"error": "Name and email are required"}), 400

    # Create new user
    new_user = User(name=data['name'], email=data['email'])

    # Add user to database
    session.add(new_user)
    session.commit()
    session.refresh(new_user) 
    session.close()
    return jsonify({"message": "User created", "user": {"id": new_user.id, "name": new_user.name, "email": new_user.email}}), 201

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
   session = SessionLocal()
   user = session.get(User, user_id)
   if user:
        session.delete(user)
        session.commit()
        return jsonify({"message": "User deleted successfully"}), 200
   else:
        return jsonify({"error": "User not found"}), 404
   
@app.route('/users/<int:user_id>', methods=['PUT'])
def put_user(user_id):
    data = request.get_json()
    session = SessionLocal()
    user = session.get(User, user_id)
    if user:
        user.name = data.get('name', user.name)  # Update name if provided
        user.email = data.get('email', user.email)
        session.commit()
        return jsonify({"message": "User updated successfully"}), 200
    else:
        return jsonify({"error": "User not found"}), 404    

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
