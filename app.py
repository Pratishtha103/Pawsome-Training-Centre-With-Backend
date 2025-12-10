from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from flask_bcrypt import Bcrypt

# Initialize Flask app and configure the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY'] = 'your hex secret code'  # Needed for flash messages
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if the user already exists
        user = User.query.filter_by(username=username).first()  # Check username
        if user:
            flash('User already exists!', 'danger')
            return redirect(url_for('signup'))

        email_user = User.query.filter_by(email=email).first()
        if email_user:
            flash('Email already registered!', 'danger')
            return redirect(url_for('signup'))

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Add the user to the database
        new_user = User(username=username, email=email, password=hashed_password)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Signup successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            flash('An error occurred. Please try again.', 'danger')

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        # Check if the user exists
        user = User.query.filter_by(email=email, username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))  # Redirect to home page
        else:
            flash('User not registered or invalid credentials.', 'danger')

    return render_template('login.html')

# Route: Dashboard (serves home.html)
@app.route('/dashboard')
def dashboard():
    return render_template('home.html')  # Render the home page

# Welcome to Pawsome backend
@app.route('/')
def welcome():
    return jsonify({"message": "Pawsome Backend is running"}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database tables if they don't exist
    app.run(debug=True)
