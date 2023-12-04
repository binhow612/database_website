from flask import Flask, render_template, request, redirect, url_for
import login
import fetch_data
import add_patient

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
    return render_template("homepage.html")

@app.route('/fetch_patient', methods = ['GET', 'POST'])
def fetch_patient_route():
    if (request.method == 'POST'):
        try:
            data = request.form
            code = data['code']
            # Call the main function in fetch_data.py
            result = fetch_data.fetch_data(code, type="P")
            if result == "Error 1":
                message = f"Error 1: No patient found with code {code}"
            elif result == "Error 2":
                message = f"Invalid patient type for patient with code {code}"
            else:
                message = {f'{key}':f'{value}' for key, value in result.items()}
            return render_template("fetch_patient_data.html", message=message)

        except Exception as e:
            return render_template("fetch_patient_data.html", message=f'Error 3: {str(e)}')
    # For GET requests, simply render the page
    return render_template("fetch_patient_data.html", message='')

@app.route('/fetch_doctor', methods = ['GET', 'POST'])
def fetch_doctor_route():
    if (request.method == 'POST'):
        try:
            data = request.form
            code = data['code']
            # Call the main function in fetch_data.py
            result = fetch_data.fetch_data(code, type="D")
            if not result:
                message = f"There is no patients treated or examined by this doctor!"
            else:
                message = result
                
            return render_template("fetch_doctor_data.html", message=message)

        except Exception as e:
            return render_template("fetch_doctor_data.html", message=f'Error 1: {str(e)}')
    # For GET requests, simply render the page
    return render_template("fetch_doctor_data.html", message='')

@app.route('/add_data', methods = ['GET', 'POST'])
def add_data_route():
    if (request.method == 'POST'):
        try:
            patient_data = request.form
            # Call the main function in add_patient.py
            result = add_patient.add_patient(patient_data)
            
            message = result
            return render_template("add_patient.html", message=message)

        except Exception as e:
            return render_template("add_patient.html", message=f'Error 2: {str(e)}')
    # For GET requests, simply render the page
    return render_template("add_patient.html", message='')


if __name__ == '__main__':
    app.run(debug=True, port=5500)
