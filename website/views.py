from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/index')
@login_required  # Ensure only authenticated users can access
def place():
    return render_template("index.html", user=current_user)
 # Pass 'user' variable

