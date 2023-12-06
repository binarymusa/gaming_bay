from flask import Flask
from flask import redirect, url_for, render_template

app = Flask(__name__)



# @app.route('/admin')
# def hello_admin():
#     return 'Hello, Admin!'

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/login')
def login_page():
   return render_template('Login.html')

@app.route('/Register')
def Register_page():
   return render_template('Registration.html')

@app.route('/About')
def About_page():
   return render_template('About.html')

@app.route('/Bookings')
def Bookings_page():
   return render_template('Bookings.html')



if __name__ == '__main__':
   app.run(debug = True)