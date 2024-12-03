from flask import Flask, render_template

from src.Controllers.UserController import UserController

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/paneladmin')
def paneladmin():
    return render_template('paneladmin.html')

@app.route('/panelcook')
def panelcook():
    return render_template('panelcook.html')

@app.route('/paneluser')
def paneluser():
    return render_template('paneluser.html')

@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/orders')
def orders():
    return render_template('orders.html')

@app.route('/shifts')
def shifts():
    return render_template('shifts.html')



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')