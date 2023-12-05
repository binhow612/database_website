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
    if request.method == "POST":
        try:
            data = request.form
            username = data['username']
            password = data['password']
            db = mysql.connector.connect(user=username, password=password, host="localhost", database="an_hospital")

            cursor = db.cursor()

            # Execute a SELECT query to fetch the user's data
            query = "SELECT * FROM doctor"
            cursor.execute(query)
            # Fetch the first row (if any)
            user_data = cursor.fetchall()

            # Check if a matching user was found
            if user_data:
                # return redirect(url_for('homepage_route'), username = username, password = password)
                return redirect(url_for('homepage_route'))

        except Exception as e:
            # return render_template("login.html", message=f'Error: {str(e)}')
            return render_template("login.html", message='Invalid username or password.')
    return render_template("login.html", message='')
    

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
            return render_template("add_patient.html", message=f"Error 2: {e}")
    # For GET requests, simply render the page
    return render_template("add_patient.html", message='')


if __name__ == '__main__':
    app.run(debug=True, port=5500)
