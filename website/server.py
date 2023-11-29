from flask import Flask, flash, render_template, request, redirect, url_for
import login

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login_route(message=None):
    message = request.args.get('message', None)
    if request.method == "POST":
        try:
            data = request.form
            username = data['username']
            password = data['password']
            option = "L"

            # Call the main function in login.py with option "L"
            result = login.main(option, username, password)

            # Check the result and set an appropriate message
            if result == "Successful":
                message = f"Login Successful for {username}!"
                return redirect(url_for('homepage_route', message=message))
            
            elif result == "Error":
                message = "Unknown error occurred."

            else:
                message = "Invalid username or password."

            return render_template("login.html", message=message)
        except Exception as e:
            return render_template("login.html", message=f'Error: {str(e)}')

    # For GET requests, simply render the login page
    return render_template("login.html", message='')

@app.route('/register', methods=['GET', 'POST'])
def register_route(message=None):
    if request.method == "POST":
        try:
            data = request.form
            username = data['newUsername']
            email = data['newEmail']
            password = data['newPassword']
            option = "R"

            # Call the main function in login.py with option "R"
            result = login.main(option, username, password, email)

            # Check the result and set an appropriate message
            if result == "Successful":
                message = f"Register Successful! Please log in to your account."
                return redirect(url_for('login_route', message=message))
      
            else:
                message = result

            return render_template("register.html", message=message)
        except Exception as e:
            return render_template("register.html", message=f'Error 2: {str(e)}')

    # For GET requests, simply render the register page
    return render_template("register.html", message='')

@app.route('/homepage')
def homepage_route():
    if request.method == "POST":
        try:
            
            pass
        except Exception as e:
            return render_template("homepage.html")

    # For GET requests, simply render the register page
    return render_template("homepage.html")

if __name__ == '__main__':
    app.run(debug=True, port=5500)