# Login Authentication Application

This is a Python Flask web application that provides user authentication features, including registration, login, logout, and password reset functionality. The application uses Flask-SQLAlchemy for database management, Flask-Login for user session management, Flask-Bcrypt for password hashing, and Flask-Mail for sending password reset emails.

## Features

1. **User Registration**:
   - Users can register by providing a unique username, email, and password.
   - Passwords are securely hashed using Bcrypt before being stored in the database.
   - Checks for duplicate usernames and emails to ensure uniqueness.

2. **User Login**:
   - Registered users can log in using their email and password.
   - Successful login redirects users to a dashboard page.
   - Failed login attempts display appropriate error messages.

3. **User Logout**:
   - Logged-in users can log out, which ends their session and redirects them to the login page.

4. **Password Reset**:
   - Users can request a password reset by providing their registered email address.
   - A password reset email is sent to the user's email address with instructions (note: the reset link in the email is a placeholder and needs to be implemented).

5. **Database**:
   - SQLite is used as the database to store user information (username, email, and hashed password).
   - The database is initialized automatically when the application runs for the first time.

6. **Email Integration**:
   - Flask-Mail is configured to send emails via Gmail's SMTP server.
   - Used for sending password reset emails (requires valid Gmail credentials).

7. **Templates**:
   - HTML templates (`register.html`, `login.html`, `dashboard.html`, `forgetpassword.html`) are used for rendering the user interface.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
## Install Dependencies

Ensure you have Python installed, then install the required packages:

```bash
pip install flask flask-sqlalchemy flask-login flask-bcrypt flask-mail
```
## Configure Email Settings

Update the app.config settings in the app.py file with your Gmail credentials:

```bash
app.config['MAIL_USERNAME'] = 'youremail@gmail.com'
app.config['MAIL_PASSWORD'] = 'yourpassword'
```
## Run the Application

Start the Flask development server:

```bash
python app.py
```
## Access the Application

  ** Register a new user at /register.

  ** Log in at /login.

  ** Access the dashboard at /dashboard (requires login).

  ** Request a password reset at /forgetpassword.

## Notes

  ** The password reset functionality currently uses a placeholder reset link (http://yourapp.com/resetpassword). You will need to implement the actual reset logic and link.

  ** Ensure that the Gmail account used for sending emails has "Allow less secure apps" enabled or uses an App Password if 2FA is enabled.
