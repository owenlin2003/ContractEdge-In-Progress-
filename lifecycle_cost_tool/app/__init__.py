from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize flask app
app = Flask(__name__, template_folder='/templates')  # Adjust the path if necessary

# Add this line to set the secret key
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a strong key

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lifecycle_cost_tool.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
