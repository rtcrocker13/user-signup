from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://get-it-done:launchcode@localhost:8889/user-signup'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

@app.route('/signin',)
def signin():
    return render_template('indexhome.html')

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)


@app.route("/", methods=['GET', 'POST'])
def index():
    email_error = ""
    password_error = ""
    verification_error = ""
    username_error = ""
    email_field = ""
    username_field = ""

    if request.method == 'POST':
        password_field = request.form['password']
        verify_field = request.form['verify']
        email_field = request.form['email']
        username_field = request.form['username']
        if email_field != "@" and "." and len(email_field) >= 20:
            email_error = "Invalid Email"
        if verify_field != password_field:
            verification_error = "Passwords DO Not Match!"
        if len(password_field) < 3 or len(password_field) >20:
            password_error = "Password Not Valid"  
        if username_field is None or username_field == "":
            username_error = "Invalid Username"
        
        hasError = email_error != "" or password_error != "" or verification_error != "" or username_error != "" 
        if not hasError:
            return redirect("/welcome?username=" + username_field)

    return render_template('indexhome.html', email_error=email_error, password_error=password_error, 
        verification_error=verification_error, username_error=username_error, email_field=email_field,
        username_field=username_field)

if __name__ == '__main__':
    app.run()