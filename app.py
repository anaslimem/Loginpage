from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, logout_user, LoginManager, login_required
from flask_bcrypt import Bcrypt
from flask_mail import Mail, Message
import os
app = Flask(__name__)
app.secret_key = "12345"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'youremail@gmail.com'
app.config['MAIL_PASSWORD'] = 'yourpassword'
app.config['MAIL_DEFAULT_SENDER'] = 'youremail@gmail.com'
mail = Mail(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(128))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
@app.route('/')
def main():
    return redirect(url_for('login'))
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        user = db.session.query(User).filter(User.username == username).first()
        user1 = db.session.query(User).filter(User.email == email).first()
        if user is None and user1 is None:
            new_user = User(username=username,email=email,password=password)
            db.session.add(new_user)
            db.session.commit()
            flash('You are now registered!', 'success')
            return redirect(url_for('login'))
        elif user1 is None:
            flash('Username already taken!', 'danger')
        else:
            flash('You are already registered!', 'warning')
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash('Login Successful!','success')
            return redirect(url_for('dashboard'))
        else:
            flash('Login Failed! Please check your credentials and try again.','danger')

    return render_template('login.html')
@app.route('/dashboard' , methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))
@app.route('/forgetpassword', methods=['GET', 'POST'])
def forgetpassword():
    if request.method == 'POST':
        email = request.form['email']
        user = db.session.query(User).filter(User.email == email).first()
        if user is None:
            flash("If an account with this email exists, a password reset email has been sent.", 'info')
        else:
            msg = Message(
                subject='Password Reset Request',
                recipients=[email],
                sender=app.config['MAIL_DEFAULT_SENDER']
            )
            msg.body = f"Hello {email},\n\nYou requested a password reset. Please click the link below to reset your password:\n\nReset Link: http://yourapp.com/resetpassword\n\nIf you did not request this, please ignore this email."
            mail.send(msg)
            flash('A password reset email has been sent to your email address.', 'success')
    return render_template('forgetpassword.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)