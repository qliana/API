from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import User  


app = Flask(__name__)

# Database configuration
DATABASE_URL = "postgresql://postgres:Quiet%402310@localhost:5433/postgres" 

# SQLAlchemy setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Route to get all users from the 'users' table
@app.route('/users', methods=['GET'])
def get_users():
    # Create a session to interact with the database
    session = SessionLocal()
    
    # Query the 'users' table to get all users
    users = session.query(User).all()
    
    # Convert the users to a list of dictionaries for easy JSON serialization
    users_list = [{"id": user.id, "name": user.name, "email": user.email} for user in users]
    
    # Close the session
    session.close()
    
    # Return the data as JSON
    return jsonify(users_list)

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)


