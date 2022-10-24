#Building a Login System with Python Flask
# base on https://morioh.com/p/c61187faa9be?f=5c21fb01c16e2556b555ab32



from flask import Flask, render_template,request,redirect,url_for,session
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'your secret key'

@app.route('/', methods=['GET', 'POST'])
def login():
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        if username=='admin'  and password=="corona":
            session['username'] = username
            return success()
        else:
            return render_template('index.html', msg='Try again')
    else:
        return render_template('index.html' , msg='') # transfer the DB to html


@app.route('/success/')
def success():
    username = session['username']
    return f"""<img src="static\LoginSuccess.jpg" alt="Cyber" width="400" height="280">
    <h1> Success Login  {username}</h1>"""

@app.route('/register/')
def register():
    return render_template('register.html' , msg='')

#if __name__ == "__main__":
#   app.run(debug=True, host="0.0.0.0" , port=80 )
