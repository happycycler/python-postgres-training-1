from src.common.database import Database
from src.models.user import User
from flask import Flask, render_template, request, session


app = Flask(__name__)
app.secret_key = "mrprice"


@app.route('/')
def hello_method():
    return render_template("login.html")
    # return "Hello, world!"


@app.before_first_request
def init_db():
    Database.initialize()


@app.route('/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    User.login_valid(email, password)
    User.login(email)

    return render_template("profile.html", email=session['email'])


if __name__ == '__main__':
    app.run(port=4995)