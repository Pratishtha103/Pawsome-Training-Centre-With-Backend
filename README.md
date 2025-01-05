# Pawsome-Training-Centre-Website
Welcome to the Pawsome Training Website repository! This project is designed to provide an online platform for dog training, where users can sign up, log in, and access home page.

#Features
Signup & Login: Users can create an account and log in to dashboard.
Frontend: Built with HTML, CSS, and JavaScript to create a user-friendly interface.
Backend: Flask Python is used to handle user authentication and data management.
Environment: Runs in a Python virtual environment to manage dependencies and keep the environment isolated.
#Tech Stack
Frontend: HTML, CSS, JavaScript
Backend: Python (Flask)
Database: SQLite3
Environment: Python 3.x, Virtual Environment (venv)
#Setup & Installation
#Prerequisites
Python 3.x installed on your system
Pip (Python package installer)
A text editor or IDE (e.g., VSCode, PyCharm)
#Steps
Clone the Repository

git clone https://github.com/Pratishtha103/pawsome-training.git
cd pawsome-training
Set up Python Virtual Environment Create a virtual environment:

python -m venv venv
Activate the virtual environment:

On Windows:
venv\Scripts\activate
On macOS/Linux:
source venv/bin/activate
Install Dependencies

pip install Flask==2.2.3
pip install Flask-SQLAlchemy==2.5.1
pip install Flask-Bcrypt==1.0.0

Run the Flask Application After setting up your environment, run the Flask app:

python app.py
The app will be accessible at http://127.0.0.1:5000/signup in your browser.

#Usage
Signup: Users can create an account by entering their email, username, and password.
Login: After signing up, users can log in using their credentials.
