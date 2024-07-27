from app import app, db, User, login_user
from flask import Flask

# Create a test client
client = app.test_client()

# Create an application context
with app.app_context():
    # Create a test user
    user = User.query.filter_by(username='your_username').first()
    
    if user:
        # Create a request context and simulate a login
        with app.test_request_context():
            with client.session_transaction() as session:
                login_user(user)
                print("User logged in:", session.get('_user_id'))
    else:
        print("User not found.")
